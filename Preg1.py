from fastapi import Depends, FastAPI

app = FastAPI()

import pyodbc
import requests
import json

#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


#@app.get("/items/")
#async def read_items(token: str = Depends(oauth2_scheme)):
#    return {"token": token}

@app.get("/SincronizacionInventario")
def Sinc(Inventory_Items_Id,Cantidad):
    direccion_servidor = '127.0.0.1'
    nombre_bd = 'AR_Holdings'
    nombre_usuario = 'AR_user'
    password = 'Credomatic65.'
    json_data = ""
    SKU = ""
    Cantidad = ""
    Imprimir = ""
    Imprimir1 = ""
    Mensaje = ""
    
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                  direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
                
        #Obtiene SKU Shopify
        url = "https://2ab146c45ec78dd0db19f3bd47cfb857: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@ar-prueba.myshopify.com/admin/api/2022-01/inventory_items.json?ids=" + Inventory_Items_Id

        payload={}
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        json_data = json.dumps(response.json())

        json_dictionary = json.loads(json_data)

        SKU = json_dictionary["inventory_items"][0]["sku"]
            
        #Obtiene Cantidad Servidor

        url2 = "https://2ab146c45ec78dd0db19f3bd47cfb857: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@ar-prueba.myshopify.com/admin/api/2022-01/inventory_levels.json?inventory_item_ids=" + Inventory_Items_Id

        payload2={}
        headers2 = {
          'Content-Type': 'application/json'
        }

        response2 = requests.request("GET", url2, headers=headers2, data=payload2)
        json_data2 = json.dumps(response2.json())

        json_dictionary2 = json.loads(json_data2)

        Cantidad = json_dictionary2["inventory_levels"][0]["available"]
        

         # Obtiene los datos del servidor de Base de datos

        with conexion.cursor() as cursor:
            cursor.execute("SELECT  Cantidad FROM [AR_Holdings].[dbo].[ColaArticulos] where SKU = '"+SKU+"'")
            Articulos = cursor.fetchall()
            # Recorrer e imprimir
            for Articulo in Articulos:
                Imprimir1 = str(Articulos[0])#["CAntidad"]

        for numero in split(Imprimir1):
           if numero.isdigit():
               Imprimir = Imprimir + str(numero)

        
        if Imprimir != "":
            
            Mensaje = "Sincronizado"
        else:
            Mensaje = "No sincronizado"
        
    except Exception as e:
        # Atrapar error
        return  str(e)
    finally:
        conexion.close()
    return Imprimir

@app.get("/Facturacion")
def Fact(SKU = None):
    return Imprimir#"Hola"

def split(word):
    return [char for char in word]

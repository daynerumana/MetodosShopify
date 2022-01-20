Create table ColaArticulos(
	ID int,
	SKU varchar(100),
	Cantidad int,
	FechaRegistro Datetime,
	FechaActualizacion DateTime,
	Sincronizado bit

	Constraint PK_ColaArticulos Primary Key (ID)
)

Create table Orden(
	ID int,
	NumeroOrden Int,
	SubTotal Decimal(16,2),
	TotalImpuestos Decimal(16,2),
	Total Decimal(16,2),
	FechaCreacion DateTime,
	FechaOrden DateTime

	Constraint PK_Orden Primary Key(ID)
)

Create table Articulos(
	ID int,
	OrdenID int,
	SKU varchar(100),
	Precio decimal(16,2),
	Cantidad int,
	Nombre varchar(150),
	Subtotal decimal(16,2),
	TotalImpuestos decimal(16,2),
	Total decimal(16,2)

	Constraint PK_Articulos Primary Key(ID),
	Constraint FK_Orden_Articulos Foreign Key (OrdenID) references Orden(ID)
)

Create table Cliente(
	ID int,
	OrdenId int,
	Nombre varchar(150),
	Apellido varchar(150),
	Email varchar(150),
	Telefono varchar(150),
	Direccion varchar(1500)

	Constraint PK_Cliente Primary Key(ID),
	Constraint FK_Orden_Cliente Foreign Key (OrdenID) references Orden(ID)
)

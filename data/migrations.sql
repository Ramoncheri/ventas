CREATE TABLE "productos" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	"tipo_producto"	TEXT NOT NULL UNIQUE,
	"precio_unitario"	REAL NOT NULL,
	"coste_unitario"	REAL NOT NULL
)
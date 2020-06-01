import csv
import sqlite3


fVentas= open('sales10.csv','r')
csvReader=csv.reader(fVentas,delimiter = ',')

conn= sqlite3.connect("data/ventas.db")  #conexion con la BBDD
c= conn.cursor()   #creamos el cursor



for linea in csvReader:
    
    
    if linea[2] != 'tipo_producto':
        a= c.execute("SELECT tipo_producto, coste_unitario from productos")
        prodBBDD= [row[0] for row in c.fetchall()]        
        print(prodBBDD)

        if linea[2] not in prodBBDD:
            c.execute("INSERT INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES ('{}', '{}', '{}')".format (linea[2], float(linea[9]), float(linea[10])))
        
        
        
        
        #try:
            #c.execute("INSERT INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES ('{}', '{}', '{}')".format (linea[2], float(linea[9]), float(linea[10])))
        #except:
            #pass

conn.commit()

conn.close()





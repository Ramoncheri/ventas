import csv
import sqlite3


fVentas= open('sales10.csv','r')
csvReader=csv.reader(fVentas,delimiter = ',')

conn= sqlite3.connect("data/ventas.db")  #conexion con la BBDD
c= conn.cursor()   #creamos el cursor

headerRow= next(csvReader)  #Coge la primera linea y ya se quita de csvReader
print(headerRow)

query= "INSERT OR IGNORE INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES (?,?,?);"

for linea in csvReader:
    datos= (linea[2], float(linea[9]), float(linea[10]))
    c.execute(query, datos)


  # otra forma:
#for linea in csvReader:
    
    #c.execute("SELECT tipo_producto  from productos")
    #prodBBDD= c.fetchall()        
    #print(prodBBDD)
    
    
    #if (linea[2],) not in prodBBDD:
     #   c.execute("INSERT INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES ('{}', '{}', '{}')".format (linea[2], float(linea[9]), float(linea[10])))
   
        
        #Una tercera forma:
        
        #try:
            #c.execute("INSERT INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES ('{}', '{}', '{}')".format (linea[2], float(linea[9]), float(linea[10])))
        #except:
            #pass

conn.commit()

conn.close()





from the_app import app
from flask import render_template, request, redirect,url_for
import csv, sqlite3
from the_app.forms import ProductForm

BBDD= './data/ventas.db'

@app.route('/')
def index():
    fVentas= open(app.config['VENTAS'],'r')
    csvReader=csv.reader(fVentas,delimiter = ',')

    
    d= {}
    for linea in csvReader:
        if linea[0] in d:
            d[linea[0]]['ingresos'] += float(linea[11])
            d[linea[0]]['beneficios'] += float(linea[13])
        else:
            if linea[0] != 'region':
                d[linea[0]]= {'ingresos': float(linea[11]), 'beneficios': float(linea[13])}

    return render_template('region.html', titulo= 'Global S.L', ventas=d)


@app.route('/paises')
def paises():
    region_name= request.values['region']  #request.value es un atributo del metodo request de Flask

    fVentas= open(app.config['VENTAS'],'r')
    csvReader=csv.reader(fVentas,delimiter = ',')
    d= {}
    for linea in csvReader:
        if linea[0]== region_name:
            if linea[1] in d:
                d[linea[1]]['ingresos'] += float(linea[11])
                d[linea[1]]['beneficios'] += float(linea[13])
            else:
                d[linea[1]]= {'ingresos': float(linea[11]), 'beneficios': float(linea[13])}
    
    return render_template('paises.html', titulo= 'Global S.L', ventas=d)

@app.route('/productos')
def productos():
    conn= sqlite3.connect(app.config['BBDD'])
    c= conn.cursor()

    query= "SELECT id, tipo_producto, precio_unitario, coste_unitario FROM productos;"
    productos= c.execute(query).fetchall()

    conn.close()
    return render_template('productos.html', productos= productos, titulo= 'Global S.L')

@app.route("/altaProducto", methods=["GET", "POST"])
def altaProducto():
    form= ProductForm()

    if request.method=='GET':
        return render_template('newProduct.html', form=form, titulo= 'Global S.L')
    else:
        conn=sqlite3.connect(app.config['BBDD'])
        c= conn.cursor()
        query= "INSERT INTO productos(tipo_producto, precio_unitario, coste_unitario) values (?,?,?);"
        datos= (request.values.get('tipo_producto'), request.values.get('precio_unitario'), request.values.get('coste_unitario'))
        c.execute(query, datos)

        conn.commit()
        conn.close()

        return redirect(url_for("productos")) #va a la ruta productos. productos es el nombre de la funcion que queremos ejecutar



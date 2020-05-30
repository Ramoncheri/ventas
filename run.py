from flask import Flask, render_template, request
import csv

app = Flask(__name__)

#mifichero= open('sales10.csv', 'r')
#linea= mifichero.readline
#while linea != '':
 #   registro= linea.split(',')



@app.route('/')
def index():
    fVentas= open('sales.csv','r')
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

    fVentas= open('sales.csv','r')
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
from flask import Flask, render_template
import csv

app = Flask(__name__)

#mifichero= open('sales10.csv', 'r')
#linea= mifichero.readline
#while linea != '':
 #   registro= linea.split(',')



@app.route('/')
def index():
    fVentas= open('sales10.csv','r')
    csvReader=csv.reader(fVentas,delimiter = ',')

    registros= []
    d= {}
    for linea in csvReader:
        registros.append(linea)
        if linea[0] in d:
            d[linea[0]]['ingresos'] += float(linea[11])
            d[linea[0]]['beneficios'] += float(linea[13])
        else:
            if linea[0] != 'region':
                d[linea[0]]= {'ingresos': float(linea[11]), 'beneficios': float(linea[13])}

    return render_template('region.html')
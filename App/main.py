"""Librerias Importadas"""
from flask import Flask
from flask import render_template
from flask import request



App=Flask(__name__)


@App.route('/')
def index():
    """Pagina Principal en donde se introduce el nombre, apellido, comision"""
    return render_template('index.html')


@App.route('/porcentaje',methods=['POST'])
def porcentaje():
    if request.method=='POST':
        """:var file: es la variable que estoy utilizando para acceder al
        archivo y copiar en el."""
        file=open("archivo.csv","w")
        """:var nombre: Donde se guarda el nombre obtenido en el html"""
        nombre=request.form['nombre']
        """:var apellido: Donde se guarda el apellido obtenido en el html"""
        apellido=request.form['apellido']
        """:var venta: la variable tipo venta se trae en tipo cadena
         y se combierte con el float para poder manipularla"""
        venta = float(request.form.get('venta'))
        if (venta > 100000):
            r = venta * 0.15
        elif (venta > 75000):
            r = venta * 0.10
        elif (venta > 50000):
            r = venta * 0.07
        elif (venta > 25000):
            r = venta * 0.05
        else:
            r = '¡Usted no ha realizado ventas en el Mes!'
        """Se esta escribiendo en el archivo csv"""
        file.write(nombre)
        file.write(",")
        file.write(apellido)
        file.write(",")
        file.write(str(venta))
        file.write(",")
        file.write(str(r))
        file.close()
        """:return render_templates: es el return que se hace para mandar los valores
        al html"""
        return render_template('porcentaje.html',nom=nombre,ape=apellido,ven=venta,rr=r)

if __name__=="__main__":
    App.run()
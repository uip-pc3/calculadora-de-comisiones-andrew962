from flask import Flask
from flask import render_template
from flask import request


App=Flask(__name__)


@App.route('/')
def index():
    return render_template('index.html')


@App.route('/porcentaje',methods=['POST'])
def porcentaje():
    if request.method=='POST':
        nombre=request.form['nombre']
        apellido=request.form['apellido']
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
        return render_template('porcentaje.html',nom=nombre,ape=apellido,ven=venta,rr=r)

if __name__=="__main__":
    App.run()
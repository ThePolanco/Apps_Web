# Importar Flask y request
from flask import Flask, render_template, request, redirect, url_for

# Crear la aplicación
app = Flask(__name__)

@app.route('/')
def index():
    datos = {
        'nombre': 'Jeison Stiven Polanco Montaño',
        'telefono': '+57 3004039815',
        'correo': 'polancojeison21@gmail.com',
        'profesion': 'Ingeniero de Sistemas',
        'especialidad': 'Análisis de Datos'
    }
    return render_template('index.html', info=datos)

@app.route('/ruta_prueba')
def ruta_prueba():
    return "Esta es una ruta de prueba."


def error_404(error):
    #return render_template('error_404.html'), 404
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.register_error_handler(404, error_404)
    app.run(debug=True, port=5544)
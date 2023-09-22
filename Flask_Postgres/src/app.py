# Importar Flask y request
from flask import Flask, render_template, request, redirect, url_for
from config import *

# Crear la aplicación
con_bd = EstablecerConexion()
app = Flask(__name__)

@app.route('/')
def index():
    cursor = con_bd.cursor()
    sql = "SELECT*FROM personas"
    cursor.execute(sql)
    PersonasRegistradas = cursor.fetchall()
    return render_template('index.html', personas = PersonasRegistradas)

# Ruta para guardar los datos
@app.route('/guardar_personas', methods=['POST'])
def agregarPersona():
    crearTablaPersonas()
    # Cursor permitira manipular la base de datos
    cursor = con_bd.cursor()
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    if nombre and apellido and telefono:
        sql = """ 
            INSERT INTO personas(nombre, apellido, telefono)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (nombre, apellido, telefono))
        con_bd.commit()
        return redirect(url_for('index'))
    else:
        return "Error en la consulta"
    
def crearTablaPersonas():
    cursor = con_bd.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personas(
            id serial NOT NULL,
            nombre character varying(30),
            apellido character varying(30),
            telefono character varying(10),
            CONSTRAINT pk_id_personas PRIMARY KEY (id)
        );
    """)
    con_bd.commit()

    
if __name__ == '__main__':
    app.run(debug=True, port=5544)
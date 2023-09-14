from flask import Flask, redirect, render_template, request, url_for
from config import *
from persona import Persona

# Instancias para realizar operaciones con la DB
con_bd = Conexion()

app = Flask(__name__)

# Ruta para guardar los datos de la DB
@app.route('/guardar_personas', methods = ['POST'])
def agregarPersona():
    personas = con_bd['Personas']
    id = request.form['id']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    telefono = request.form['telefono']

    if id and nombre and apellido and edad and telefono:
        persona = Persona(id, nombre, apellido, edad, telefono)
        # insert_one para crear un documento en Mongo
        personas.insert_one(persona.formato_doc())
        return redirect(url_for('index'))
    else:
        return "Error"

# Ruta para eliminar documentos
@app.route('/eliminar_persona/<string:id_persona>')
def eliminar(id_persona):
    personas = con_bd['Personas']
    # Se hara uso del metodo delete_one() para eliminar un documento con un criterio especifico
    personas.delete_one({'id': id_persona}) 
    return redirect(url_for('index'))
       
# Ruta para actualizar registros
@app.route('/editar_persona/<string:id_persona>', methods = ['POST'])
def editar(id_persona):
    personas = con_bd['Personas']
    # Se realiza el mismo proceso de inserción y extracción para poder actualizar los datos
    id = request.form['id']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    telefono = request.form['telefono']
    # Utilizaremos la función update_one()
    if id and nombre and apellido and edad and telefono:
        personas.update_one({'id': id_persona}, 
                            {'$set': {'id' : id ,'nombre' : nombre , 'apellido': apellido, 'edad': edad, 'telefono': telefono}}) # update_one() necesita de al menos dos parametros para funcionar
        return redirect(url_for('index'))
    else:
        return "Error"
    
       
# Ruta para el index
@app.route('/')
def index():
    # Consultar datos de la colección mediante la función find()
    personas = con_bd['Personas']
    # Para identificar todas las personas registradas
    PersonasRegistradas = personas.find()
    # Para identificar las personas registradas que son mayores de edad
    Mayores_de_18 = personas.find({"edad":{"$gt": 18}})
    # Para identificar las personas por un criterio en especifico
    Apellido = personas.find({"apellido":"Rincon"})
    # Para identificar las personas con un rango de edad
    Rango_Edad = personas.find({"edad": {"$gt": 0, "$lt": 19}})
    # Para identificar las personas que su nombre con que inicia con J, la opción i permite ignorar si la letra es mayuscula o minuscula
    Letra_Inicial = personas.find({"nombre": {"$regex": "^J", "$options": "i"}})
    # Para limitar los registros mostrados
    Limite = personas.find().limit(3) 
    
    return render_template('index.html',personas = PersonasRegistradas, 
                                        personas_mayores = Mayores_de_18, 
                                        busqueda_apellido = Apellido,
                                        rangos = Rango_Edad,
                                        letra = Letra_Inicial,
                                        limitar = Limite)
    

if __name__ == '__main__':
    app.run(debug = True, port = 2001)
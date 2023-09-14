# Crear y almacenar objetos en la base de datos

class Persona:
    def __init__(self, id, nombre, apellido, edad, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)
        self.telefono = telefono
    
    # Metodo para almacenar los documentos
    def formato_doc(self):
        return{
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'telefono': self.telefono    
        }    
    
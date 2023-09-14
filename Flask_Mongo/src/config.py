from pymongo import MongoClient
import certifi

# Conexión con MongoDB
MONGO = 'mongodb+srv://jspolanco:polanco@cluster.ii2izzv.mongodb.net/?retryWrites=true&w=majority'

# Utilización del certificado
certificado = certifi.where()

# Función para la conexión con la DB
def Conexion():
    try:
        client = MongoClient(MONGO, tlsCAFile = certificado)
        bd = client["bd_personas"]
    except ConnectionError:
        print("Error de Conexión")
    return bd


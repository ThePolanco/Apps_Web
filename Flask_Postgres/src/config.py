from psycopg2 import connect

HOST= 'localhost'
PORT = 5432
BD = 'bd_personas'
USUARIO = 'postgres'
PASSWORD = 'Luxray08'

def EstablecerConexion():
    try:
        conexion = connect(host=HOST, port=PORT,
                         dbname=BD, user=USUARIO, password=PASSWORD)
    except ConnectionError:
        print("Error de Conexion")
    return conexion
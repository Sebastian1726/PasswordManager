import pyodbc
from dotenv import load_dotenv
import os

class DataLayer:
    def __init__(self):
        load_dotenv()
        server = os.getenv('DB_SERVER')
        database = os.getenv('DB_NAME')
        username = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        try:
            self.conn = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={server};'
                f'DATABASE={database};'
                f'UID={username};'
                f'PWD={password}'
            )
            self.cursor = self.conn.cursor()
        except pyodbc.Error as e:
            print("Error al conectar a la base de datos:", e)
            raise

    def agregar_contrasena(self, sitio_web, nombre_usuario, contrasena_encriptada):
        query = "INSERT INTO Contrasenas (SitioWeb, NombreUsuario, Contrasena) VALUES (?, ?, ?)"
        self.cursor.execute(query, sitio_web, nombre_usuario, contrasena_encriptada)
        self.conn.commit()

    def obtener_contrasenas(self):
        query = "SELECT Id, SitioWeb, NombreUsuario, Contrasena FROM Contrasenas"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def actualizar_contrasena(self, id_contrasena, sitio_web, nombre_usuario, contrasena_encriptada):
        query = "UPDATE Contrasenas SET SitioWeb = ?, NombreUsuario = ?, Contrasena = ? WHERE Id = ?"
        self.cursor.execute(query, sitio_web, nombre_usuario, contrasena_encriptada, id_contrasena)
        self.conn.commit()

    def eliminar_contrasena(self, id_contrasena):
        query = "DELETE FROM Contrasenas WHERE Id = ?"
        self.cursor.execute(query, id_contrasena)
        self.conn.commit()
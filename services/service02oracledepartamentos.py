import oracledb
from models import departamento

class ServiceDepartamentos():
    def __init__(self):
        #Inicializamos la conexion directamente con esto
        self.connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

    def insertarDepartamento(self, numero, nombre, localidad):
        #Hacemos funciones de entrar y salir
        cursor = self.connection.cursor() #Entramos al cursor
        sql = "INSERT INTO DEPT VALUES (:num, :nom, :loc)"
        cursor.execute(sql, (numero, nombre, localidad,))
        self.connection.commit() #Guardamos si es lo que queremos
        registros = cursor.rowcount
        cursor.close() #Salimos
        return registros #Devolvemos el resultado
    
    def eliminarDepartamento(self, id):
        cursor = self.connection.cursor()
        sql = "DELETE FROM DEPT WHERE DEPT_NO = :iddepartamento"
        cursor.execute(sql, (id,))
        self.connection.commit()
        borrados = cursor.rowcount
        cursor.close()
        return borrados    
    
    def updateDepartamento(self, id, nombre, localidad):
        cursor = self.connection.cursor()
        sql = "UPDATE DEPT SET DNOMBRE = :nombre2, LOC = :loc2 WHERE DEPT_NO = :iddept"
        cursor.execute(sql, (nombre, localidad, id,))
        self.connection.commit()
        actualizados = cursor.rowcount
        cursor.close()
        return actualizados
    
    def getNombreDepartamento(self, id):
        cursor = self.connection.cursor()
        sql = "SELECT DNOMBRE FROM DEPT WHERE DEPT_NO = :id"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        nombre = row[0]
        cursor.close()
        return nombre
    
    def getNombreLocalidadDepartamento(self, id):
        cursor = self.connection.cursor()
        sql = "SELECT DNOMBRE, LOC FROM DEPT WHERE DEPT_NO = :id"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        nombre = row[0]
        localidad = row[1]
        cursor.close()
        return nombre
    
    def getDepartamento(self, id):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM DEPT WHERE DEPT_NO = :id"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        #Creamos un nuevo departamento
        dept = departamento.Departamento()
        dept.idDepartamento = row[0]
        dept.nombre = row[1]
        dept.localizacion = row[2]
        cursor.close()
        return dept
    
    def getListaDepartamentos(self):
        cursor = self.connection.cursor() 
        sql = "SELECT * FROM DEPT"
        cursor.execute(sql)
        #Necesitamos una lista para guardar cada DEPT
        listaDepartamentos = []
        for row in cursor:
            #Por cada fila, creamos un objeto departamento
            dept = departamento.Departamento()
            dept.idDepartamento = row[0]
            dept.nombre = row[1]
            dept.localizacion = row[2]
            #Añadimos a la lista cada dept
            listaDepartamentos.append(dept)
        cursor.close()
        return listaDepartamentos

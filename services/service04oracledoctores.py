import oracledb
from models import doctores as models

class ServiceDoctores:

    def __init__(self):
        #Inicializamos la conexion directamente con esto
        self.connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

    def insertarDoctor(self, idHos, nombre, especialidad, salario):
        cursor = self.connection.cursor()
        sql = "SELECT MAX(DOCTOR_NO) + 1 AS MAXIMO FROM DOCTOR"
        cursor.execute(sql)
        row = cursor.fetchone()
        idDoc = row[0]
        sql = "INSERT INTO DOCTOR VALUES (:idhos, :idDoc, :nom, :espe, :dinero)"
        cursor.execute(sql, (idHos, idDoc, nombre, especialidad, salario,))
        self.connection.commit()
        cursor.close()

    def getDoctores(self):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM DOCTOR"
        cursor.execute(sql)
        #Creamos la lista donde se van a guardar los objetos
        listaDoctores = []
        for row in cursor:
            doctor = models.Doctor()
            doctor.idHospital = row[0]
            doctor.idDoctor = row[1]
            doctor.nombre = row[2]
            doctor.especialidad = row[3]
            doctor.salario = row[4]
            listaDoctores.append(doctor)
        cursor.close()
        return listaDoctores
    
    def updateDoctor(self, idDoc, nombre, especialidad, salario):
        cursor = self.connection.cursor()
        sql = "UPDATE DOCTOR SET APELLIDO = :nom, ESPECIALIDAD = :espe, SALARIO = :money WHERE DOCTOR_NO = :id"
        cursor.execute(sql, (nombre, especialidad, salario, idDoc,))
        self.connection.commit()
        cursor.close()

    def deleteDoctor(self, id):
        cursor = self.connection.cursor()
        sql = "DELETE FROM DOCTOR WHERE DOCTOR_NO = :id"
        cursor.execute(sql, (id,))
        self.connection.commit()
        cursor.close()

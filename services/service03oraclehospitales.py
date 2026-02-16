import oracledb
from models import hospital as models

class ServiceHospitales:

    def __init__(self):
        #Inicializamos la conexion directamente con esto
        self.connection = oracledb.connect(user = "SYSTEM", password = "oracle", dsn = "localhost/FREEPDB1")

    #Metodo para recuperar todos los hospitales
    def getHospitales(self):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM HOSPITAL"
        cursor.execute(sql)
        #Creamos el objeto para guardar los datos
        listaHospitales = []
        for row in cursor:
            hospital = models.Hospital()
            hospital.idHospital = row[0]
            hospital.nombre = row[1]
            hospital.direccion = row[2]
            hospital.telefono = row[3]
            hospital.camas = row[4]
            listaHospitales.append(hospital)
        cursor.close()
        return listaHospitales
    
    def insertarHospital(self, id, nombre, dir, tlf, camas):
        cursor = self.connection.cursor()
        sql = "INSERT INTO HOSPITAL VALUES(:id, :nom, :direc, :telf, :cam)"
        cursor.execute(sql, (id, nombre, dir, tlf, camas,))
        self.connection.commit()
        cursor.close()

    def updateHospitales(self, id, nom, dir, tlf, camas):
        cursor = self.connection.cursor()
        sql = "UPDATE HOSPITAL SET NOMBRE = :nom, DIRECCION = :dir, TELEFONO = :tlf, NUM_CAMA = :cam WHERE HOSPITAL_COD = :id"
        cursor.execute(sql, (nom, dir, tlf, camas, id,))
        self.connection.commit()
        cursor.close()

    def deleteHospital(self, id):
        cursor = self.connection.cursor()
        sql = "DELETE FROM HOSPITAL WHERE HOSPITAL_COD = :id"
        cursor.execute(sql, (id,))
        self.connection.commit()
        cursor.close()

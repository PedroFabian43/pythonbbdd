import mssql_python

connection = mssql_python.connect('Server=sqlpaco3430.database.windows.net;Database=AZURETAJAMAR;Encrypt=yes;UID=adminsql;PWD=Admin123;TrustServerCertificate=yes')
print("Funciona SQL Server")
sql = "select * from EMP"
cursor = connection.cursor()
cursor.execute(sql)
for row in cursor:
    print(f"{row[1]}")
cursor.close()
connection.close()
print("Fin de programa")
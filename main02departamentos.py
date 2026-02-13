#Existe la posibilidad d eponer un alias a los nombres llamados NameSpaces
from services import service02oracledepartamentos as serv
print("Bienvenido a mi Servicio Departamentos")
 #creamos la clase servicio
servicio = serv.ServiceDepartamentos()
#Queremos hacer un menu simple

print("-----Menu de Viernes-----")
print("1.- Insertar departamento")
print("2.- Mostrar departamentos")
print("Seleccione opción")
opcion = int(input())

if (opcion == 1):
    #Codigo de insertar
    print("Insertar departamento")
    numero = int(input("ID departamento: "))
    nombre = input("Nombre departamento: ")
    localidad = input("Localidad: ")
    reg = servicio.insertarDepartamento(numero, nombre, localidad)
    print(f"Insertados: {reg}")
else:
    #Codigo de mostrar
    print("----Lista Departamentos----")
    lista = servicio.getListaDepartamentos()
    for dept in lista:
        print(f"{dept.idDepartamento} - {dept.nombre} - {dept.localizacion}")

# print("Insertar departamento")
# numero = int(input("ID departamento: "))
# nombre = input("Nombre departamento: ")
# localidad = input("Localidad: ")
# reg = servicio.insertarDepartamento(numero, nombre, localidad)
# print(f"Insertados: {reg}")
# print("Dime un departamento a eliminar")
# id = int(input())
# bor = servicio.eliminarDepartamento(id)
# print(f"Eliminados: {reg}")

# print("----Actualizar Departamentos----")
# idDept = int(input("Dime el número de departamento a modificar: "))
# new_nombre = input("Dime el nuevo nombre del departamento: ")
# new_loc = input("Dime donde se desplaza el departamento: ")

# act = servicio.updateDepartamento(idDept, new_nombre, new_loc)
# print(f"Departamentos actualizados: {act}")

# print("----Datos Departamento----")
# print("Departamento a buscar:")
# id = int(input())
# dept = servicio.getDepartamento(id)
# print(f"Nombre: {dept.nombre}, Localidad: {dept.localizacion}")

# print("----Lista Departamentos----")
# lista = servicio.getListaDepartamentos()
# for dept in lista:
#     print(f"{dept.idDepartamento} - {dept.nombre} - {dept.localizacion}")


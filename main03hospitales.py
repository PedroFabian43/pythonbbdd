from services import service03oraclehospitales as services
service = services.ServiceHospitales()

#Creamos un método para mostrar la lista de hospitales
def mostrarHospitales():
    lista = service.getHospitales()
    print("----Lista de hospitales----")
    for hospital in lista:
        print(f"Id: {hospital.idHospital} / Nombre: {hospital.nombre} / Dirección: {hospital.direccion} / Teléfono: {hospital.telefono} / Num.casa: {hospital.camas}")
        print("--------------------------------------------------------------------------------------------------")

print("Bienvenido a mi servicio de hospitales")

print("-----CRUD Hospitales-----")
print("1.- Insertar Hospital")
print("2.- Mostrar Hospitales")
print("3.- Modificar Datos")
print("4.- Eliminar Hospital")
print("Seleccione una opción:")
opcion = int(input())
if(opcion == 1):
    id = int(input("Id del nuevo hospital: "))
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    camas = int(input("Número de camas: "))
    service.insertarHospital(id, nombre, direccion, telefono, camas)
    mostrarHospitales()
elif (opcion == 2):
    mostrarHospitales()
elif (opcion == 3):
    id = int(input("Id del Hospital a modificar: "))
    nombre = input("Nuevo nombre: ")
    direccion = input("Nueva dirección: ")
    telefono = input("Nuevo teléfono: ")
    camas = int(input("Número de camas: "))
    service.updateHospitales(id, nombre, direccion, telefono, camas)
    mostrarHospitales()
elif (opcion == 4):
    id = int(input("Id del Hospital a eliminar: "))
    service.deleteHospital(id)
    mostrarHospitales()

print("Fin de programa")

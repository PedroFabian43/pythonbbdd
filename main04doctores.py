from services import service04oracledoctores as serv

service = serv.ServiceDoctores()

def mostrarDoctores():
    lista = service.getDoctores()
    print("----Lista de Doctores----")
    for doctor in lista:
        print(f"Id_Hospital: {doctor.idHospital} / Num_Doctor: {doctor.idDoctor} / Nombre: {doctor.nombre} / Especialidad: {doctor.especialidad} / Salario: {doctor.salario}")
        print("--------------------------------------------------------------------------------------------------")

def menuDoctores():
    print("-----Plantilla de Doctores-----")
    print("¿Que desea hacer?")
    print("1.- Insertar Doctor")
    print("2.- Mostrar Doctores")
    print("3.- Modificar Datos")
    print("4.- Eliminar Doctor")
    print("5.- Salir de la aplicación")
    print("Seleccione una opción:")

bucleMenu = False
opcion = 0
while(bucleMenu != True):
    menuDoctores()
    opcion = int(input())

    if (opcion >= 6 or opcion <= 0):
        print("Has salido de la aplicación")
        break

    if(opcion == 1):
        id = int(input("Dime el Id del Hospital: "))
        num_doc = int(input("Dime el número de Doctor: "))
        nombre = input("Dime el nombre: ")
        funcion = input("Dime su especialidad: ")
        salario = int(input("Dime cuanto gana: "))
        service.insertarDoctor(id, num_doc, nombre, funcion, salario)
        mostrarDoctores()

    elif(opcion == 2):
        mostrarDoctores()

    elif(opcion == 3):
        idDoc = int(input("Dime el Id del doctor a modificar: "))
        nombre = input("Dime el nombre: ")
        funcion = input("Dime su especialidad: ")
        salario = int(input("Dime cuanto gana: "))
        service.updateDoctor(idDoc, nombre, funcion, salario)
        mostrarDoctores()

    elif(opcion == 4):
        id = int(input("Dime el id del Doctor a eliminar: "))
        service.deleteDoctor(id)
        mostrarDoctores()

print("Fin de Programa")
from services import service04sqlserverdoctores as serv
import os

service = serv.ServiceDoctores()

def mostrarDoctores():
    lista = service.getDoctores()
    print("----Lista de Doctores----")
    for doctor in lista:
        print(f"Id_Hospital: {doctor.idHospital} \nNum_Doctor: {doctor.idDoctor} \nNombre: {doctor.nombre} \nEspecialidad: {doctor.especialidad} \nSalario: {doctor.salario}")
        print("----------------------------------")

def menuDoctores():
    print("-----Base de Datos de Doctores-----")
    print("¿Que desea hacer?")
    print("1.- Insertar Doctor")
    print("2.- Mostrar Doctores")
    print("3.- Modificar Datos")
    print("4.- Eliminar Doctor")
    print("5.- Salir de la aplicación")
    print("Seleccione una opción:")

def clear():
    os.system("clear")

clear()
bucleMenu = False
opcion = 0
while(bucleMenu != True):
    menuDoctores()
    opcion = int(input())

    if (opcion == 5):
        clear()
        break

    if(opcion == 1):
        id = int(input("Dime el Id del Hospital: "))
        nombre = input("Dime el nombre: ")
        funcion = input("Dime su especialidad: ")
        salario = int(input("Dime cuanto gana: "))
        service.insertarDoctor(id, nombre, funcion, salario)
        clear()
        print("Doctor añadido con éxito")
        mostrarDoctores()

    elif(opcion == 2):
        clear()
        mostrarDoctores()

    elif(opcion == 3):
        idDoc = int(input("Dime el Id del doctor a modificar: "))
        nombre = input("Dime el nombre: ")
        funcion = input("Dime su especialidad: ")
        salario = int(input("Dime cuanto gana: "))
        service.updateDoctor(idDoc, nombre, funcion, salario)
        clear()
        print("Datos modificados con éxito")
        mostrarDoctores()

    elif(opcion == 4):
        id = int(input("Dime el id del Doctor a eliminar: "))
        service.deleteDoctor(id)
        clear()
        print("Doctor eliminado con éxito")
        mostrarDoctores()
    
    else:
        clear()
        print("Opción inválida. Elige una opción diferente")

print("has salido de la aplicación")
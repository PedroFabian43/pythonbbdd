from models import mascota

#Vamos a tener un simple método para llamarlo desde el main
def getSaludo():
    return "Hoy es juernes"

def getMascota():
    dato = mascota.Mascota()
    dato.nombre = "Flounder"
    dato.raza = "Pez"
    dato.edad = 22
    return dato
def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "Nala"
    dato.raza = "Leona"
    dato.edad = 18
    return dato


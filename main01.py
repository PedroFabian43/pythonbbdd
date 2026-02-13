from services import service01prueba
print("Soy un Main")
texto = service01prueba.getSaludo()
pez = service01prueba.getMascota()
leona = service01prueba.getMascota2()
print(f"{pez.nombre}, Raza: {pez.raza}, Edad: {pez.edad}")
print(leona.nombre)
print(texto)



anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
anio_actual = 2026

if (anio_nacimiento % 4 == 0 and anio_nacimiento % 100 != 0) or anio_nacimiento % 400 == 0:
    print("El año de nacimiento es bisiesto")
else:
    print("El año de nacimiento no es bisiesto")

edad = anio_actual - anio_nacimiento

print("Edad:", edad)

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
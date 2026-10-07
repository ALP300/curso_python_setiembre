nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
categoria = input("Ingrese la categoría (tecnología, alimentos, ropa): ").lower()

if categoria == "tecnología" or categoria == "tecnologia":

    if precio > 2000:
        impuesto = precio * 0.18
        clasificacion = "Lujo"
    else:
        impuesto = precio * 0.10
        clasificacion = "Estándar"

elif categoria == "alimentos":

    if precio > 100:
        impuesto = precio * 0.05
        clasificacion = "Premium"
    else:
        impuesto = 0
        clasificacion = "Básico"

elif categoria == "ropa":

    if precio > 500:
        impuesto = precio * 0.15
        clasificacion = "Lujo"
    else:
        impuesto = precio * 0.08
        clasificacion = "Básico"

else:
    print("Categoría no válida")
    impuesto = 0
    clasificacion = "Sin clasificación"

precio_final = precio + impuesto

print("\nProducto:", nombre)
print("Categoría:", categoria)
print("Clasificación:", clasificacion)
print("Precio original:", precio)
print("Impuesto:", impuesto)
print("Precio final:", precio_final)
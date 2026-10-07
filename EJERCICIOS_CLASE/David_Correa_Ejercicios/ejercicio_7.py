numero = input("Ingrese un número entero: ")

pares = 0
impares = 0

for digito in numero:
    if int(digito) % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Cantidad de dígitos pares:", pares)
print("Cantidad de dígitos impares:", impares)
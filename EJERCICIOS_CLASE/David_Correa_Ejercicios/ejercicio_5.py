n = int(input("Ingrese un número: "))

suma = 0

print("Múltiplos encontrados:")

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        suma += i

print("La suma de los múltiplos es:", suma)
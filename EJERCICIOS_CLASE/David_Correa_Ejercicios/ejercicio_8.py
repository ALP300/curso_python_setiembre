def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))

print("Números primos en el rango:")

for numero in range(inicio, fin + 1):
    if es_primo(numero):
        print(numero)
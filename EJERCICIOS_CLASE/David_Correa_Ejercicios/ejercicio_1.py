nota = float(input("Ingrese su nota (0-20): "))
asistencia = float(input("Ingrese su porcentaje de asistencia: "))

if nota >= 11 and asistencia >= 70:
    print("Resultado: Aprobado")

    if nota > 17 and asistencia == 100:
        print("Mención especial: Excelente rendimiento!")
else:
    print("Resultado: Desaprobado")
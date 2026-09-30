'''
Sistema de clasificación de rendimiento: 
Solicita al usuario su nota (0-20) y su asistencia (%). Si la nota 
es mayor o igual a 11 y 
la asistencia es mayor o igual al 70%, se aprueba. De lo contrario, 
se desaprueba. 
Además, otorga menciones especiales para notas mayores a 17 con 
asistencia completa.
'''
nota= int(input("Ingresa la nota de la persona: "))
asistencia= int(input("Ingresa la asistencia de la persona: "))

if nota>=11 and asistencia>=70:
    print("Aprobaste")
    if nota>=17 and asistencia==100:
        print("CRACKKKKKK, MENCIÓN ESPECIAL")
    else:
        print("Biennnn, felicidades!")

else:
    print("Desaprobaste")









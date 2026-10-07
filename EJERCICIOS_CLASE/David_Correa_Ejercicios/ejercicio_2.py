usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")
rol = input("Ingrese su rol: ")   

if usuario == "admin" and contraseña == "admin" and rol == "admin":
    print("Permisos de admin: CRUD completo")
elif usuario == "editor" and contraseña == "editor" and rol == "editor":
    print("Permisos de editor: Crear y editar")
elif usuario == "visitante" and contraseña == "visitante" and rol == "visitante":
    print("Permisos de visitante: Solo leer")
else:
    print("Credenciales inválidas")
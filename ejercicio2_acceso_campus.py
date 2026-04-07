# Credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
acceso = False

# 1, 2 y 3) Login con máximo 3 intentos
while intentos < 3:
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        break
    else:
        intentos += 1
        print(f"Datos incorrectos. Intentos restantes: ({3 - intentos})")

if not acceso:
    print("Cuenta bloqueada")
else:
    # 4) Menú repetitivo
    opcion = ""
    while opcion != "4":
        print("\n--- MENÚ ---")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mensaje motivacional")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        # 5) Validación
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            print("Error. Ingrese un número entre 1 y 4.")
            opcion = input("Seleccione una opción: ")

        # Opciones
        if opcion == "1":
            print("Estado: Inscripto")
        elif opcion == "2":
            nueva_clave = input("Ingrese nueva clave: ")
            # Validar longitud
            while len(nueva_clave) < 6:
                print("Error. Debe tener al menos 6 caracteres.")
                nueva_clave = input("Ingrese nueva clave: ")
            confirmar = input("Confirme la nueva clave: ")
            while nueva_clave != confirmar:
                print("Error. Las claves no coinciden.")
                confirmar = input("Confirme la nueva clave: ")
            clave_correcta = nueva_clave
            print("Clave actualizada correctamente")
        elif opcion == "3":
            print("Con esfuerzo y dedicación es posible lograr todo lo que te propongas.")
        elif opcion == "4":
            print("Saliendo del sistema...")
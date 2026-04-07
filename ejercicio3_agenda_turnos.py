# Turnos vacíos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

# 1) Nombre del operador
operador = input("Ingrese su nombre: ")
while not operador.isalpha():
    print("Error. Solo letras.")
    operador = input("Ingrese su nombre: ")

opcion = ""

# Menú principal
while opcion != "5":
    print("\n--- MENU ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    opcion = input("Seleccione opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error. Ingrese un número entre 1 y 5.")
        opcion = input("Seleccione opción: ")

    # 1. RESERVAR TURNO
    if opcion == "1":
        dia = input("Día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error. Ingrese 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ")
        nombre = input("Nombre del paciente: ")
        while not nombre.isalpha():
            print("Error. Solo letras.")
            nombre = input("Nombre del paciente: ")

        if dia == "1":  # Lunes
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Ya tiene turno el lunes")
            elif lunes1 == "":
                lunes1 = nombre
                print("Turno reservado en Lunes")
            elif lunes2 == "":
                lunes2 = nombre
                print("Turno reservado en Lunes")
            elif lunes3 == "":
                lunes3 = nombre
                print("Turno reservado en Lunes")
            elif lunes4 == "":
                lunes4 = nombre
                print("Turno reservado en Lunes")
            else:
                print("No hay cupos el lunes")
        else:  # Martes
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Ya tiene turno el martes")
            elif martes1 == "":
                martes1 = nombre
                print("Turno reservado en Martes")
            elif martes2 == "":
                martes2 = nombre
                print("Turno reservado en Martes")
            elif martes3 == "":
                martes3 = nombre
                print("Turno reservado en Martes")
            else:
                print("No hay cupos el martes")

    # 2. CANCELAR TURNO
    elif opcion == "2":
        dia = input("Día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error. Ingrese 1 o 2.")
            dia = input("Día (1=Lunes, 2=Martes): ")
        nombre = input("Nombre a cancelar: ")
        while not nombre.isalpha():
            print("Error. Solo letras.")
            nombre = input("Nombre a cancelar: ")

        if dia == "1":  # Lunes
            if lunes1 == nombre:
                lunes1 = ""
            elif lunes2 == nombre:
                lunes2 = ""
            elif lunes3 == nombre:
                lunes3 = ""
            elif lunes4 == nombre:
                lunes4 = ""
            else:
                print("No se encontró el turno")
                continue
            print("Turno cancelado")
        else:  # Martes
            if martes1 == nombre:
                martes1 = ""
            elif martes2 == nombre:
                martes2 = ""
            elif martes3 == nombre:
                martes3 = ""
            else:
                print("No se encontró el turno")
                continue
            print("Turno cancelado")

    # 3. VER AGENDA DEL DÍA
    elif opcion == "3":
        dia = input("Dia (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            print("Error. Ingrese 1 o 2.")
            dia = input("Dia (1=Lunes, 2=Martes): ")
        if dia == "1":
            print("\nLUNES")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("\nMARTES")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    # 4. RESUMEN GENERAL
    elif opcion == "4":
        ocup_lunes = 0
        if lunes1 != "": ocup_lunes += 1
        if lunes2 != "": ocup_lunes += 1
        if lunes3 != "": ocup_lunes += 1
        if lunes4 != "": ocup_lunes += 1
        ocup_martes = 0
        if martes1 != "": ocup_martes += 1
        if martes2 != "": ocup_martes += 1
        if martes3 != "": ocup_martes += 1

        print(f"Lunes: {ocup_lunes} ocupados, {4 - ocup_lunes} libres")
        print(f"Martes: {ocup_martes} ocupados, {3 - ocup_martes} libres")
        if ocup_lunes > ocup_martes:
            print("Día con más turnos: Lunes")
        elif ocup_martes > ocup_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate")

    elif opcion == "5":
        print("Sistema cerrado")
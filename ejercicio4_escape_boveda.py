energia = 100
tiempo = 12
cerraduras = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

# Nombre del agente
nombre = input("Ingrese su nombre de agente: ")
while not nombre.isalpha():
    print("Error: Solo letras.")
    nombre = input("Ingrese su nombre de agente: ")

print(f"\nBienvenido agente {nombre}. Tienes 100 de energía y 12 horas.")

while energia > 0 and tiempo > 0 and cerraduras < 3 and not alarma:
    print("\n" + "-"*40)
    print(f"Energía: {energia} | Tiempo: {tiempo}h | Cerraduras: ({cerraduras}/3) | Alarma: {'ON' if alarma else 'OFF'}")
    print("-"*40)
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = input("\nAcción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese 1, 2 o 3.")
        opcion = input("Acción: ")

    if opcion == "1":  # Forzar cerradura
        racha_forzar += 1
        energia -= 20
        tiempo -= 2

        if racha_forzar >= 3:
            alarma = True
            print("¡La cerradura se trabó! Alarma activada.")
        elif energia < 40:
            print("Riesgo de alarma...")
            riesgo = input("Elegí 1-3 (3 = peligro): ")
            while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                riesgo = input("Elegí 1-3 (3 = peligro): ")
            if riesgo == "3":
                alarma = True
                print("¡Activaste la alarma!")
        else:
            cerraduras += 1
            print(f"Cerradura abierta! ({cerraduras}/3)")

    elif opcion == "2":  # Hackear panel
        racha_forzar = 0
        energia -= 10
        tiempo -= 3
        print("Hackeando panel...")
        for i in range(4):
            print(f"Paso {i+1}/4 ...")
            codigo_parcial += "A"
            print(f"Código parcial: {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras < 3:
            cerraduras += 1
            print(f"Cerradura abierta automáticamente! ({cerraduras}/3)")

    elif opcion == "3":  # Descansar
        racha_forzar = 0
        tiempo -= 1
        energia = min(100, energia + 15)
        if alarma:
            energia -= 10
            print("Descansaste, pero la alarma te drena energia extra.")
        else:
            print("Descansaste y recuperaste energia.")

    # Verificar bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras < 3:
        print("\n¡El sistema se bloqueó por la alarma!")
        break

# Resultado final
print("\n" + "=="*40)
if cerraduras == 3:
    print("¡VICTORIA! Abriste la bóveda a tiempo.")
elif alarma and tiempo <= 3:
    print("DERROTA: El sistema se bloqueó por la alarma.")
else:
    print("DERROTA: Te quedaste sin energia o tiempo.")
print("=="*40)
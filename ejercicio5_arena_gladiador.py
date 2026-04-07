# Paso 1: Nombre del Gladiador
nombre = input("Ingrese el nombre de su Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras")
    nombre = input("Ingrese el nombre de su Gladiador: ")

# Paso 2: Estadísticas iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
daño_pesado = 15
daño_enemigo = 12
turno_jugador = True

print(f"\n¡Bienvenido a la Arena, Gladiador {nombre}!\n")

# Ciclo principal de combate
while vida_jugador > 0 and vida_enemigo > 0:
    print("-" * 50)
    print(f"{nombre}: {vida_jugador} HP | Enemigo: {vida_enemigo} HP | Pociones: {pociones}")
    print("-" * 50)

    # Menú del jugador
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    opcion = input("Elige tu acción (1-3): ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese un número entre 1 y 3")
        opcion = input("Elige tu acción (1-3): ")

    # Turno del Jugador
    if opcion == "1":  # Ataque Pesado
        if vida_enemigo < 20:
            daño = daño_pesado * 1.5  # Golpe Crítico (float)
            print(f"¡GOLPE CRÍTICO!")
        else:
            daño = daño_pesado
        vida_enemigo -= daño
        print(f"¡Atacaste al enemigo por {daño} puntos de daño!")

    elif opcion == "2":  # Ráfaga Veloz
        print("¡Ráfaga Veloz!")
        for i in range(3):
            vida_enemigo -= 5
            print(f" > Golpe conectado por 5 de daño")

    elif opcion == "3":  # Curar
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Te curaste 30 HP. Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones! Pierdes el turno.")

    # Turno del Enemigo (siempre ataca después del jugador)
    if vida_jugador > 0 and vida_enemigo > 0:
        vida_jugador -= daño_enemigo
        print(f"¡El enemigo te atacó por {daño_enemigo} puntos de daño!")

# Fin del juego
print("\n" + "=" * 50)
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
print("=" * 50)
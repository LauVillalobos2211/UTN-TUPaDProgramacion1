# 1) Nombre del cliente
nombre_cliente = input("Ingrese el nombre del cliente: ")
while not nombre_cliente.isalpha():
    print("Error, ingrese solo letras")
    nombre_cliente = input("Ingrese su nombre: ")

# 2) Cantidad de productos
cantidad_productos = input("Ingrese la cantidad de productos: ")
while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
    print("Error ingrese solo números: ")
    cantidad_productos = input("Ingrese la cantidad de productos: ")

cantidad = int(cantidad_productos)
total_sin_descuentos = 0
total_con_descuentos = 0

# 3) Cargar productos
for i in range(cantidad):
    print(f"\nProducto {i+1}")
    precio = input("Ingrese el precio del producto: ")
    while not precio.isdigit():
        print("Error, ingrese un número entero")
        precio = input("Ingrese el precio del producto: ")
    precio = int(precio)
    total_sin_descuentos += precio

    descuento = input("¿Tiene descuento? (S/N): ").lower()
    while descuento not in ["s", "n"]:
        print("Error, ingrese S o N.")
        descuento = input("¿Tiene descuento? (S/N): ").lower()

    if descuento == "s":
        precio_con_descuento = precio * 0.9
    else:
        precio_con_descuento = precio
    total_con_descuentos += precio_con_descuento

# 4) Resultados finales
ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

print("\n--- Resumen ---")
print(f"Cliente: {nombre_cliente}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
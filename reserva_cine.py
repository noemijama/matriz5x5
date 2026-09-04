# Programa para gestionar la reserva de asientos en una sala de cine
# Autor: Noemi Jama
# Objetivo: Reservar un asiento por fila y columna y mostrar el estado de la sala
# Fecha: 04 de septiembre de 2026

# 1. Crear la matriz de 3 filas x 4 columnas, todos libres (valor 0)
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# 2. Solicitar al usuario los datos del asiento a reservar
print("=== Sistema de Reserva de Asientos ===")
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# --- Validación opcional de rango ---
if 0 <= fila <= 2 and 0 <= columna <= 3:
    # 3. Marcar como reservado si está libre
    if asientos[fila][columna] == 0:
        asientos[fila][columna] = 1
        print("\nAsiento en fila", fila, ", columna", columna, "reservado con éxito.\n")
    else:
        print("\nEl asiento fila", fila, ", columna", columna, "ya estaba reservado.\n")
else:
    print("\nValores fuera de rango. Filas: 0–2 | Columnas: 0–3")
    exit()  # Terminar el programa si los datos no son válidos

# 4. Mostrar el estado completo de la sala con bucles anidados
print("Estado de la sala (0 = Libre / 1 = Reservado):")
for i in range(3):               # Recorrer cada fila
    for j in range(4):           # Recorrer cada columna de la fila
        print(asientos[i][j], end=" ")  # Imprimir en la misma línea
    print()                       # Salto de línea al terminar la fila
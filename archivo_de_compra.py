def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total


if __name__ == "__main__":
    precio_producto = 10
    cantidad_productos = 3
    total_a_pagar = calcular_total(precio_producto, cantidad_productos)
    print(f"El total a pagar es: {total_a_pagar}")
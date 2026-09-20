# Función con parámetros y retorno de valor
def calcular_promedio(nota1, nota2, nota3):
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    return promedio  # Retorno obligatorio


# Programa principal
print("=== Cálculo de Promedio de Notas ===")
n1 = float(input("Ingresa la primera nota: "))
n2 = float(input("Ingresa la segunda nota: "))
n3 = float(input("Ingresa la tercera nota: "))

# Llamada a la función
resultado = calcular_promedio(n1, n2, n3)

# Mostrar resultado
print(f"\nEl promedio es: {resultado:.2f}")
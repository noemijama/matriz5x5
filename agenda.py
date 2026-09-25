# ======================================================
# Programa: Agenda de Contactos
# Autor: Estudiante
# Descripción: Gestión básica de contactos usando diccionarios
# ======================================================

# ----------------------
# 1. Crear la colección de datos
# Usamos un diccionario: clave = nombre, valor = teléfono
# ----------------------
agenda = {}

# ----------------------
# 2. Función para agregar contactos
# ----------------------
def agregar_contacto(nombre, telefono):
    agenda[nombre] = telefono
    print(f"✅ Contacto '{nombre}' agregado correctamente.")

# ----------------------
# 3. Función para mostrar todos los contactos
# ----------------------
def mostrar_contactos():
    if not agenda:
        print("📋 La agenda está vacía.")
        return
    print("\n=== Lista de Contactos ===")
    for nombre, telefono in agenda.items():
        print(f"👤 {nombre}: 📞 {telefono}")
    print("==========================\n")

# ----------------------
# 4. Función para buscar un contacto
# ----------------------
def buscar_contacto(nombre):
    if nombre in agenda:
        print(f"🔍 Encontrado: {nombre} → {agenda[nombre]}")
    else:
        print(f"❌ El contacto '{nombre}' no existe.")

# ----------------------
# 5. Función para eliminar un contacto
# ----------------------
def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"🗑️ Contacto '{nombre}' eliminado.")
    else:
        print(f"❌ No se puede eliminar: '{nombre}' no está en la agenda.")

# ----------------------
# 6. Ejecución / Pruebas del programa
# ----------------------
if __name__ == "__main__":
    # Agregar datos de ejemplo
    agregar_contacto("Ana", "0987654321")
    agregar_contacto("Luis", "0991234567")
    agregar_contacto("María", "0974567890")

    # Mostrar todos
    mostrar_contactos()

    # Buscar un contacto
    buscar_contacto("Luis")
    buscar_contacto("Carlos")

    # Eliminar un contacto
    eliminar_contacto("Ana")
    
    # Mostrar después de eliminar
    print("--- Agenda tras eliminar ---")
    mostrar_contactos()
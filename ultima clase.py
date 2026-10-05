# ==============================================
# Gestor de Contactos - Uso de Colecciones de Datos
# Estructuras utilizadas: Diccionario y Lista
# ==============================================

# ----------------------
# 1. Crear la colección de datos
# Diccionario principal: clave = nombre, valor = teléfono
contactos = {}
# Lista para llevar un orden de registro
orden_registro = []

# ----------------------
# 2. Función para agregar datos
def agregar_contacto(nombre, telefono):
    if nombre not in contactos:
        contactos[nombre] = telefono
        orden_registro.append(nombre)
        print(f"✅ Contacto '{nombre}' agregado correctamente.")
    else:
        print(f"⚠️ El contacto '{nombre}' ya existe.")

# ----------------------
# 3. Función para mostrar todos los datos
def mostrar_contactos():
    print("\n=== Lista de Contactos ===")
    if not contactos:
        print("No hay contactos registrados.")
        return
    for nombre in orden_registro:
        print(f"Nombre: {nombre:15} | Teléfono: {contactos[nombre]}")
    print(f"Total de contactos: {len(contactos)}")

# ----------------------
# 4. Operación adicional: Buscar contacto
def buscar_contacto(nombre):
    if nombre in contactos:
        print(f"🔍 Encontrado: {nombre} → Teléfono: {contactos[nombre]}")
        return True
    else:
        print(f"❌ El contacto '{nombre}' no existe.")
        return False

# ----------------------
# 5. Operación adicional: Eliminar contacto
def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        orden_registro.remove(nombre)
        print(f"🗑️ Contacto '{nombre}' eliminado.")
    else:
        print(f"❌ No se puede eliminar: '{nombre}' no está registrado.")

# ----------------------
# 6. Ejecución / Prueba del programa
if __name__ == "__main__":
    # Agregar datos de ejemplo
    agregar_contacto("Ana Pérez", "0987654321")
    agregar_contacto("Luis Gómez", "0912345678")
    agregar_contacto("María López", "0998765432")
    
    # Mostrar todos
    mostrar_contactos()
    
    # Buscar un contacto
    print("\n--- Búsqueda ---")
    buscar_contacto("Luis Gómez")
    buscar_contacto("Carlos Ruiz")
    
    # Eliminar un contacto
    print("\n--- Eliminación ---")
    eliminar_contacto("Ana Pérez")
    
    # Mostrar actualizado
    mostrar_contactos()
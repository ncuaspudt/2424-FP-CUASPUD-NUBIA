
# Vamos a crear un Diccionario con información personal verídica de una persona.
informacion_personal = {
    "nombre": "Javier Muñoz",
    "edad": 38,
    "ciudad": "Urcuqui",
    "profesion": "Licenciado"
}


# Acceder y Modificar Valores
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")  # Imprimir la ciudad actual
informacion_personal["ciudad"] = "Ibarra"  # Modificar la ciudad
print(f"Ciudad modificada: {informacion_personal['ciudad']}")

# Agregar una nueva clave-valor
informacion_personal["profesion"] = "Ingeniero"  # Cambiar la profesión
print(f"Profesión modificada: {informacion_personal['profesion']}")

# Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0939338296"  # Agregar número de teléfono ficticio

# Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminar la clave "edad"

# Imprimir el Diccionario Final
print("Diccionario final:", informacion_personal)
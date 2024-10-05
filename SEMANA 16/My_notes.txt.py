# Escritura de Archivo de Texto

# Crear un nuevo archivo llamado my_notes.txt
my_notes = open('my_notes.txt', 'w')

# Escribir al menos tres líneas de notas personales en el archivo
my_notes.write("Nota 1: Comprar para el refrigerio.\n")
my_notes.write("Nota 2: Llamar a Luis para confirmar la reunión de beca.\n")
my_notes.write("Nota 3: Comprar materiales para el trabajo de fisica.\n")

# Cerrar el archivo después de escribir
my_notes.close()

# Lectura de Archivo de Texto

# Abrir el archivo my_notes.txt
my_notes = open('my_notes.txt', 'r')

# Leer el contenido del archivo línea por línea utilizando readline()
print('Contenido de my_notes.txt:')
for _ in range(3):  # Sabemos que hay tres líneas
    linea = my_notes.readline()  # Leer una línea del archivo
    print(linea.strip())  # Mostrar cada línea leída, eliminando el salto de línea

# Cerrar el archivo
my_notes.close()

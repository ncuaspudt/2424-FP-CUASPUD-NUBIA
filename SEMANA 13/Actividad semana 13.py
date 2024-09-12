def temperatura_promedio(ciudades_temperaturas):
    """
    Esta función calcula la temperatura promedio de un conjunto de ciudades.
    Args:
        ciudades_temperaturas (dict): Un diccionario que contiene nombres de ciudades como claves
                                      y listas de temperaturas como valores.
    Returns:
        dict: Un diccionario que contiene nombres de ciudades como claves
              y temperaturas promedio como valores.
    """
    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Creamos un diccionario de cinco ciudades y diferentes temperaturas diarias.
ciudades_temperaturas = {
    "Quito": [22, 24, 23, 25, 26],
    "Urcuqui": [28, 35, 29, 33, 30],
    "Ibarra": [21, 23, 22, 24, 25],
    "Riobamba": [30, 32, 31, 33, 34],
    "Guaranda": [29, 31, 30, 31, 32]
}


# Esta función  calculara las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")
def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante el período dado.

    Parámetros:
    temperaturas (list): Una matriz 3D donde la primera dimensión es ciudades,
                          la segunda es días de la semana, y la tercera es semanas.
                          Cada elemento es un diccionario con la temperatura del día.

    Retorna:
    dict: Un diccionario donde las claves son los nombres de las ciudades y los valores
          son el promedio de temperaturas durante el período.
    """
    promedios = {}

    # Iterar sobre las ciudades
    for i, ciudad in enumerate(temperaturas):
        total_temperaturas = 0
        cantidad_dias = 0

        # Iterar sobre las semanas
        for semana in ciudad:
            for dia in semana:
                total_temperaturas += dia['temp']
                cantidad_dias += 1

        # Calcular el promedio para la ciudad
        promedio = total_temperaturas / cantidad_dias
        promedios[f"Ciudad {i + 1}"] = promedio

    return promedios


# Uso de la función con datos de ejemplo
promedios = calcular_temperatura_promedio(temperaturas)
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: Promedio de temperaturas = {promedio:.2f}")

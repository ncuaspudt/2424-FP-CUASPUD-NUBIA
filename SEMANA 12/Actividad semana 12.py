# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (2 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (2 semanas)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 27}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 36}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 35}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(temperaturas):
    print(f"Ciudad {i + 1}:")
    for j, semana in enumerate(ciudad):
        suma = 0
        for dia in semana:
            suma += dia['temp']
        promedio = suma / len(semana)  # 7 días por semana
        print(f"  Semana {j + 1}: Promedio de temperaturas = {promedio:.2f}")

# Definición de función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el monto del descuento
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Llamar a la función 1
monto_total_1 = 800  # Compra de $800
descuento_1 = calcular_descuento(monto_total_1)  # Llamada a la función
monto_final_1 = monto_total_1 - descuento_1  # Monto final después del descuento

# Imprimir resultados de la primera llamada
print(f'Compra 1: Monto total = ${monto_total_1}')
print(f'Descuento (10%) = ${descuento_1:.2f}')  # Monto del descuento
print(f'Monto final a pagar = ${monto_final_1:.2f}')  # Monto final después del descuento

print()  # Línea vacía para separar resultados

# Llamar a la función 2
monto_total_2 = 1000  # Compra de $1000
descuento_2 = calcular_descuento(monto_total_2, 15)  # Usar 15% de descuento
monto_final_2 = monto_total_2 - descuento_2  # Monto final después del descuento

# Imprimir resultados de la segunda llamada
print(f'Compra 2: Monto total = ${monto_total_2}')
print(f'Descuento (15%) = ${descuento_2:.2f}')  # Monto del descuento
print(f'Monto final a pagar = ${monto_final_2:.2f}')  # Monto final después del descuento
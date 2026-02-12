def convertir_temperatura(celsius):
    """
    Convierte grados Celsius a Fahrenheit y Kelvin
    """
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Pruebas Ejercicio 1
print("=" * 50)
print("EJERCICIO 1: CONVERSIÓN DE TEMPERATURAS")
print("=" * 50)
temp_c = 25
f, k = convertir_temperatura(temp_c)
print(f"{temp_c}°C = {f}°F y {k}K")

temp_c = 0
f, k = convertir_temperatura(temp_c)
print(f"{temp_c}°C = {f}°F y {k}K")




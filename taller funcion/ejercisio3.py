def analizar_ventas(lista_ventas):
    mayor = max(lista_ventas)
    menor = min(lista_ventas)
    promedio = sum(lista_ventas) / len(lista_ventas)
    return mayor, menor, promedio


print("\n" + "=" * 50)
print("EJERCICIO 3: ANÁLISIS DE VENTAS")
print("=" * 50)

ventas = [12000000000, 8500000000, 1020000, 210000, 1750, 980]
print(f"Ventas: {ventas}")

mayor, menor, prom = analizar_ventas(ventas)

print(f"\nVenta mayor: ${mayor}")
print(f"Venta menor: ${menor}")
print(f"Promedio de ventas: ${prom:.2f}")

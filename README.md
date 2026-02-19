[taller funtion python.py](https://github.com/user-attachments/files/25422809/taller.funtion.python.py)
ZONAS = {
    "Marbella": {"km": 10, "tarifa": 10_000},
    "Torices":  {"km": 15, "tarifa": 25_000},
    "Biciroma": {"km": 30, "tarifa": 70_000},
    "Centro":   {"km": 5,  "tarifa": 8_000},
    "Torcos":   {"km": 20, "tarifa": 40_000},
}
REPARTIDORES = {
    "forero":     ["Centro"],
    "brayan":     ["Torices", "Marbella"],
    "ian": ["Biciroma"],
    "Bleyder":  ["bocagrande"],
}
pedidos = []

def procesar_pedido(nombre, direccion, telefono, zona):
    if zona not in ZONAS:
        print(f"Zona '{zona}' no encontrada"); return

    info = ZONAS[zona]
    rep  = next((r for r, z in REPARTIDORES.items() if zona in z), None)
    p    = {
        "id": len(pedidos) + 1,
        "cliente": {"nombre": nombre, "direccion": direccion, "telefono": telefono},
        "zona": zona, "repartidor": rep, "tarifa": info["tarifa"],
    }
    pedidos.append(p)

    print(f"\n{'='*40}")
    print(f" Pedido #{p['id']} → {nombre} | {zona} | {info['km']} km | ${info['tarifa']:,}")
    print(f" Repartidor: {rep or 'Sin asignar'}")
    print(f"{'='*40}")
    return p

if __name__ == "__main__":
    procesar_pedido("Carlos", "Cra 5 #10-20",  "3001234567", "Torices")
    procesar_pedido("Ana",    "Cl 30 #8-15",   "3119876543", "Marbella")
    procesar_pedido("Pedro",  "Av 1 #20-30",   "3201112233", "Centro")
    procesar_pedido("María",  "Cra 10 #5-40",  "3154445566", "Biciroma")
    procesar_pedido("Juan",   "Cl 50 #15-10",  "3107778899", "Torcos")

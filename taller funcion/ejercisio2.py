def agregar_estudiante(estudiantes, nombre, nota):
    estudiante = {"nombre": nombre, "nota": nota}
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} agregado exitosamente")

def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    print("\nLista de estudiantes:")
    for i, est in enumerate(estudiantes, 1):
        print(f"{i}. {est['nombre']} - Nota: {est['nota']}")

def calcular_promedio(estudiantes):
    if not estudiantes:
        return 0
    suma = sum(est['nota'] for est in estudiantes)
    return suma / len(estudiantes)

# Uso
estudiantes = []
agregar_estudiante(estudiantes, "Juan", 4.5)
agregar_estudiante(estudiantes, "María", 3.8)
mostrar_estudiantes(estudiantes)
print(f"Promedio: {calcular_promedio(estudiantes):.2f}")
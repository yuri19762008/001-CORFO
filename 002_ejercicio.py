

# Lista para almacenar los datos de los estudiantes
estudiantes = []

# Solicitar datos de los cinco estudiantes
for i in range(5):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} para {nombre}: "))
        notas.append(nota)
    estudiantes.append([nombre, notas])

# Calcular y mostrar el promedio de cada estudiante
print("\nPromedios de los estudiantes:")
for estudiante in estudiantes:
    nombre = estudiante[0]
    notas = estudiante[1]
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
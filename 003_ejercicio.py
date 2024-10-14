# Función para validar las notas ingresadas
def validar_nota(nota):
    try:
        nota = float(nota)
        if 1 <= nota <= 7:
            return True
        else:
            print("La nota debe estar entre 1 y 7.")
            return False
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return False

# Lista para almacenar los datos de los estudiantes
estudiantes = []

# Solicitar datos de los cinco estudiantes
for i in range(5):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    notas = []
    for j in range(3):
        while True:
            nota = input(f"Ingrese la nota {j+1} para {nombre}: ")
            if validar_nota(nota):
                notas.append(float(nota))
                break
    estudiantes.append([nombre, notas])

# Calcular y mostrar el promedio de cada estudiante
print("\nPromedios de los estudiantes:")
for estudiante in estudiantes:
    nombre = estudiante[0]
    notas = estudiante[1]
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
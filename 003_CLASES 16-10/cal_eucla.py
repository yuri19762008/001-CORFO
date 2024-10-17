import math

# Definir la función lambda para la distancia euclidiana
distancia_euclidiana = lambda x1, y1, x2, y2: math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Recibir las coordenadas desde la entrada estándar
x1 = float(input("Ingrese la coordenada x1: "))
y1 = float(input("Ingrese la coordenada y1: "))
x2 = float(input("Ingrese la coordenada x2: "))
y2 = float(input("Ingrese la coordenada y2: "))

# Calcular la distancia utilizando la función lambda
distancia = distancia_euclidiana(x1, y1, x2, y2)

# Imprimir el resultado
print(f"La distancia euclidiana entre los puntos es: {distancia}")
0

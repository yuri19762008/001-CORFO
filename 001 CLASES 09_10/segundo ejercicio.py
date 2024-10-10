

x1, y1 = map(float, input("Ingresa las coordenadas del primer punto (x1, y1): ").split())
x2, y2 = map(float, input("Ingresa las coordenadas del segundo punto (x2, y2): ").split())

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"La distancia euclidiana entre ({x1}, {y1}) y ({x2}, {y2}) es {distancia}")

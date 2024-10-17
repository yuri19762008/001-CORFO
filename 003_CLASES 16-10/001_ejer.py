# Creamos una lista de ejemplo
numeros = [5, 12, 8, 3, 9, 21, 4, 15]

# Usamos reduce() para encontrar el valor mayor
from functools import reduce

valor_mayor = reduce(lambda x, y: x if x > y else y, numeros)

# Imprimimos el resultado
print(f"El valor mayor en la lista {numeros} es: {valor_mayor}")
#calculo raiz cuadrada

numero = float(input("Ingresa un número: "))
aproximacion = [(numero / 2 + numero / (numero / 2)) / 2 for _ in range(10)][-1]
print(f"La raíz cuadrada aproximada de {numero} es {aproximacion}")



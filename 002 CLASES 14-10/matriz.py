import numpy as np

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

def ingresar_matriz():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor para la posición ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    
    return np.array(matriz)

def menu():
    print("\n--- Calculadora de Matrices ---")
    print("1. Suma de matrices")
    print("2. Resta de matrices")
    print("3. Multiplicación de matrices")
    print("4. Determinante")
    print("5. Inversa")
    print("6. Transpuesta")
    print("7. Rango")
    print("8. Traza")
    print("9. Valores propios")
    print("10. Vectores propios")
    print("0. Salir")
    return input("Seleccione una opción: ")

def main():
    while True:
        opcion = menu()
        
        if opcion == "0":
            print("Gracias por usar la calculadora de matrices. ¡Hasta luego!")
            break
        
        elif opcion in ["1", "2", "3"]:
            print("\nIngrese la primera matriz:")
            matriz1 = ingresar_matriz()
            print("\nIngrese la segunda matriz:")
            matriz2 = ingresar_matriz()
            
            if opcion == "1":
                resultado = matriz1 + matriz2
                print("\nResultado de la suma:")
            elif opcion == "2":
                resultado = matriz1 - matriz2
                print("\nResultado de la resta:")
            else:
                resultado = np.dot(matriz1, matriz2)
                print("\nResultado de la multiplicación:")
            
            imprimir_matriz(resultado)
        
        elif opcion in ["4", "5", "6", "7", "8", "9", "10"]:
            print("\nIngrese la matriz:")
            matriz = ingresar_matriz()
            
            if opcion == "4":
                print(f"\nDeterminante: {np.linalg.det(matriz)}")
            elif opcion == "5":
                try:
                    inversa = np.linalg.inv(matriz)
                    print("\nMatriz inversa:")
                    imprimir_matriz(inversa)
                except np.linalg.LinAlgError:
                    print("La matriz no es invertible.")
            elif opcion == "6":
                print("\nMatriz transpuesta:")
                imprimir_matriz(matriz.T)
            elif opcion == "7":
                print(f"\nRango de la matriz: {np.linalg.matrix_rank(matriz)}")
            elif opcion == "8":
                print(f"\nTraza de la matriz: {np.trace(matriz)}")
            elif opcion == "9":
                valores_propios = np.linalg.eigvals(matriz)
                print("\nValores propios:")
                print(valores_propios)
            else:
                valores_propios, vectores_propios = np.linalg.eig(matriz)
                print("\nVectores propios:")
                imprimir_matriz(vectores_propios)
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
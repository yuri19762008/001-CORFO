import math
from typing import List, Union

def obtener_numeros(cantidad: int) -> List[float]:
    """Solicita al usuario ingresar la cantidad especificada de números."""
    numeros = []
    for i in range(cantidad):
        while True:
            try:
                num = float(input(f"Ingrese el número {i + 1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Por favor ingrese un número válido.")
    return numeros

class CalculadoraLambda:
    def __init__(self):
        # Operaciones básicas y de comparación
        self.operaciones = {
            1: ("Suma", lambda nums: sum(nums)),
            2: ("Resta", lambda nums: nums[0] - sum(nums[1:])),
            3: ("Multiplicación", lambda nums: eval('*'.join(map(str, nums)))),
            4: ("División", lambda nums: nums[0] / nums[1] if nums[1] != 0 else "Error: División por cero"),
            5: ("Promedio", lambda nums: sum(nums) / len(nums)),
            6: ("Potencia", lambda nums: nums[0] ** nums[1]),
            7: ("Raíz Cuadrada", lambda nums: [math.sqrt(n) for n in nums]),
            8: ("Valor Absoluto", lambda nums: [abs(n) for n in nums]),
            9: ("Números Pares/Impares", lambda nums: [(n, "Par" if n % 2 == 0 else "Impar") for n in nums]),
            # Nuevas operaciones de comparación
            10: ("Encontrar el Mayor", lambda nums: max(nums)),
            11: ("Encontrar el Menor", lambda nums: min(nums)),
            12: ("Ordenar de Menor a Mayor", lambda nums: sorted(nums)),
            13: ("Ordenar de Mayor a Menor", lambda nums: sorted(nums, reverse=True)),
            14: ("Análisis Completo de Comparación", lambda nums: {
                "Mayor": max(nums),
                "Menor": min(nums),
                "Promedio": sum(nums) / len(nums),
                "Cantidad de números": len(nums),
                "Números mayores al promedio": len([n for n in nums if n > sum(nums)/len(nums)]),
                "Números menores al promedio": len([n for n in nums if n < sum(nums)/len(nums)])
            })
        }

    def mostrar_menu(self):
        print("\n=== CALCULADORA CON FUNCIONES LAMBDA ===")
        print("\n--- Operaciones Básicas ---")
        for key in range(1, 10):
            print(f"{key}. {self.operaciones[key][0]}")
        print("\n--- Operaciones de Comparación ---")
        for key in range(10, 15):
            print(f"{key}. {self.operaciones[key][0]}")
        print("0. Salir")

    def ejecutar_operacion(self, opcion: int, numeros: List[float]) -> Union[float, str, List, dict]:
        if opcion in self.operaciones:
            nombre, operacion = self.operaciones[opcion]
            resultado = operacion(numeros)
            
            # Formato especial para el análisis completo
            if opcion == 14:
                return nombre, self.formatear_analisis_completo(resultado)
            return nombre, resultado
        return "Operación inválida", None

    def formatear_analisis_completo(self, resultado: dict) -> str:
        """Formatea el resultado del análisis completo de manera legible."""
        return "\n".join([
            f"• {key}: {value}"
            for key, value in resultado.items()
        ])

def main():
    calculadora = CalculadoraLambda()
    
    while True:
        try:
            calculadora.mostrar_menu()
            opcion = int(input("\nSeleccione una operación (0 para salir): "))
            
            if opcion == 0:
                print("¡Gracias por usar la calculadora!")
                break
                
            if opcion not in calculadora.operaciones:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                continue

            # Determinar cantidad de números necesarios para la operación
            if opcion == 4:  # División
                cantidad = 2
            elif opcion == 6:  # Potencia
                cantidad = 2
            else:
                cantidad = int(input("¿Cuántos números desea procesar? "))
                if cantidad <= 0:
                    print("Por favor ingrese una cantidad válida.")
                    continue

            numeros = obtener_numeros(cantidad)
            nombre_operacion, resultado = calculadora.ejecutar_operacion(opcion, numeros)

            print("\n=== RESULTADO ===")
            print(f"Operación: {nombre_operacion}")
            print(f"Números ingresados: {numeros}")
            if isinstance(resultado, (list, dict)):
                print("Resultado:")
                print(resultado)
            else:
                print(f"Resultado: {resultado}")
            
            continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()
            if continuar != 's':
                print("¡Gracias por usar la calculadora!")
                break

        except ValueError:
            print("Error: Por favor ingrese un número válido.")
        except Exception as e:
            print(f"Error: {str(e)}")
            continue

if __name__ == "__main__":
    main()
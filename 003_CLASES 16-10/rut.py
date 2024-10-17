# Función lambda para calcular el dígito verificador del RUT
digito_verificador = lambda rut: '0' if (11 - sum(int(d) * f for d, f in zip(reversed(rut), [2, 3, 4, 5, 6, 7] * 10)) % 11) == 11 else 'K' if (11 - sum(int(d) * f for d, f in zip(reversed(rut), [2, 3, 4, 5, 6, 7] * 10)) % 11) == 10 else str(11 - sum(int(d) * f for d, f in zip(reversed(rut), [2, 3, 4, 5, 6, 7] * 10)) % 11)

# Pedir el RUT al usuario en formato sin puntos ni guiones
rut = input("Ingrese el RUT sin puntos ni el dígito verificador: ")

# Calcular el dígito verificador
dv = digito_verificador(rut)

# Imprimir el dígito verificador calculado
print(f"El dígito verificador para el RUT {rut} es: {dv}")

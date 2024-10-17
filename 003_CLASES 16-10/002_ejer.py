# Ejercicio 2 - Registro de vientos con conversión usando lambda
# Solicitamos datos de la estación
nombre_estacion = input("Ingrese el nombre de la estación de monitoreo: ")

# Solicitamos los vientos en nudos para diferentes horas
vientos_nudos = {
    "últimas 5 horas": float(input("Ingrese viento (nudos) hace 5 horas: ")),
    "últimas 10 horas": float(input("Ingrese viento (nudos) hace 10 horas: ")),
    "últimas 15 horas": float(input("Ingrese viento (nudos) hace 15 horas: "))
}

# Usamos lambda con map para convertir nudos a km/h
vientos_kmh = dict(zip(
    vientos_nudos.keys(),
    map(lambda nudos: nudos * 1.852, vientos_nudos.values())
))

print("\nResultados para la estación:", nombre_estacion)
print("\nVientos registrados:")
for tiempo, velocidad in vientos_kmh.items():
    print(f"- {tiempo}: {velocidad:.2f} km/h")
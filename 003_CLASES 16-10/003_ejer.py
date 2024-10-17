# Ejercicio 3 - Filtrado de vientos altos usando lambda
nombre_estacion = input("Ingrese el nombre de la estación de monitoreo: ")

# Solicitamos los vientos en nudos
vientos_nudos = {
    "últimas 5 horas": float(input("Ingrese viento (nudos) hace 5 horas: ")),
    "últimas 10 horas": float(input("Ingrese viento (nudos) hace 10 horas: ")),
    "últimas 15 horas": float(input("Ingrese viento (nudos) hace 15 horas: "))
}

# Convertimos a km/h usando lambda con map
vientos_kmh = dict(zip(
    vientos_nudos.keys(),
    map(lambda nudos: nudos * 1.852, vientos_nudos.values())
))

# Mostramos todos los vientos
print("\nResultados para la estación:", nombre_estacion)
print("\nTodos los vientos registrados:")
for tiempo, velocidad in vientos_kmh.items():
    print(f"- {tiempo}: {velocidad:.2f} km/h")

# Filtramos vientos > 20 km/h usando lambda
vientos_altos = dict(filter(lambda x: x[1] > 20, vientos_kmh.items()))

print("\nVientos que sobrepasan 20 km/h:")
if vientos_altos:
    for tiempo, velocidad in vientos_altos.items():
        print(f"¡ALERTA! {tiempo}: {velocidad:.2f} km/h")
else:
    print("No se registraron vientos superiores a 20 km/h")
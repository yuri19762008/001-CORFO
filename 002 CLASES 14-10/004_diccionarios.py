# otro ejercicio 

personas = []
flag = True
while flag:
    nombre = input("Nombre (o 'FIN' para terminar): ")
    if nombre.lower() == "fin":
        flag = False
    else:
        apellido = input("Apellido: ")
        curso = input("Nombre del curso: ")
        notas = [float(input(f"Nota {i+1}: ")) for i in range(3)]
        
        personas.append({
            "nombre": nombre,
            "apellido": apellido,
            "cursos": {curso: notas}
        })

print("\nResumen:")
for p in personas:
    print(f"\n{p['nombre']} {p['apellido']}")
    for curso, notas in p['cursos'].items():
        promedio = sum(notas) / len(notas)
        print(f"  {curso}: {promedio:.2f}")



print ("--------------------------------")


#INVENTARIO

inventario = {
    "chaqueat-01" : {"cantidad" : 20, "precio" : 20990 },
    "pantalon-01 " : {"cantiadad" : 10 , "precio" : 19990}
}

for i in range(2):
    nombre = input ("ingrese el nombre del producto ")
    cantidad = input ("ingrese el cantidad del producto ")
    precio = input ("ingrese el precio del producto ")
    
if nombre not in inventario:
    inventario[nombre] = {"cantidad ": cantidad, "precio" : precio}
else:
    print("error : clave existente")
 
print("inventario completo ")

for nombre in inventario:
    print(f"Producto: {nombre}, cantidad: {inventario[nombre]['cantidad']}, precio: {inventario[nombre]['precio']}")




print ("--------------------------------")



#EJERCICIO

personas = []

while True:
    nombre = input("Ingrese el nombre (o 'FIN' para terminar): ")
    if nombre == "FIN":
        break
    
    apellido = input("Ingrese el apellido: ")
    
    persona = {
        "nombre": nombre,
        "apellido": apellido
    }
    
    personas.append(persona)

print("\nLista de personas registradas:")
for persona in personas:
    print(f"Nombre: {persona['nombre']}, Apellido: {persona['apellido']}")
    
    

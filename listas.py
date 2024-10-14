







productos = ["zapatillas", "chalecos", "zapatos", "pantalones"]

for i in range(3):
    nuevo_producto = input("Ingrese Nuevo Producto:")
    productos.append(nuevo_producto)

producto_a_eliminar = input("Ingrese el nombre del producto a eliminar: ")
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
else:
    print("error, no existe")


productos.sort()

print("el inventario de producto es ", productos)
print("primer elemento: ", productos[0])
print ("ultimo elemento:" , productos[5])





id = input("id del producto: ")
nombre = input("nombre del producto: ")
descripcion = input("descripcion del producto: ")
costo = int(input("costo del producto: "))
precio = costo / ((1-0.30))
cantidad = input("cantidad del producto: ")
estado = input("estado del producto: ")



print(f"ID:{id}\n Nombre:{nombre}\n Descripcion:{descripcion}\n Costo:{costo}\n Cantidad:{cantidad}\n Estado:{estado}\n Precio:{precio}\n")


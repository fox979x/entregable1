




producto = { "id":1, "nombre": "alpinito", "precio":1500, "cantidad":20, "estado":"disponible"}

print(producto["nombre"])

producto.update({"cantidad":15})

print(producto["cantidad"])

print(len(producto))

for key, value in producto.items():
    print(key, value)
    
usuario = {}

id_user = int(input("ingrese el id"))
usuario.update({"id":id_user})
name_user = input("nombre")
usuario.update({"nombre":name_user})
email_user = input("correo")
usuario.update({"mail":email_user})
clave = input("clave")

print(usuario)

usuario.popitem()

print(usuario)
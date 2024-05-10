usuarios = []
contador = 0
while contador < 5:



    usuario = []
    nombre = input("Ingrese nombre: ")
    usuario.append(nombre)
    apellido = input("Ingrese apellido: ")
    usuario.append(apellido)
    telefono = input("Ingrese teléfono: ")
    usuario.append(telefono)
    correo = input("Ingrese correo electrónico: ")
    usuario.append(correo)
    clave = input("Ingrese clave: ")
    usuario.append(clave)
    
    usuarios.append(usuario)
    
    usuarios.append(usuario)
    
    contador += 1

print("Nombre\t\tApellido\tTeléfono\tCorreo\t\t\tClave")
for usuario in usuarios:
    print("\t".join(usuario))


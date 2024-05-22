


clientes = {}

def registrar_clientes():

    id_user = int(input("ingrese el id"))
    name_user = input("nombre")
    email_user = input("correo")
    clave = input("clave")
    clientes[id_user] = ({"nombre":name_user,"mail":email_user,"clave":clave})

def ver_clientes():
    for key, value in clientes.items():
        print(key, value)

registrar_clientes();
registrar_clientes();
ver_clientes();

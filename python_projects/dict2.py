

usuarios = {}

#esta funcion registra usuarios

def registrar_usuario():

    id_user = int(input("ingrese el id"))
    name_user = input("nombre")
    email_user = input("correo")
    clave = input("clave")
    usuarios[id_user] = ({"nombre":name_user,"mail":email_user,"clave":clave})
    
# esta funcion llama un for e itera el diccionario

def ver_usuario():
    for key, value in usuarios.items():
        print(key, value)

registrar_usuario();
registrar_usuario();
ver_usuario();





usar = "pp@mail.com"
key = 1234
tel = 3193416857

usuario = input("Usuario")

clave = int(input("clave"))

telefono =  int(input("telefono"))

# Usando if else cree un sistema de login que valide las credenciales, si cumple permita iniciar 
# y si no, que imprima un mensaje de validar credenciales

if usuario == usar and telefono == tel or clave == key :
    print("Bienvenido")
else:
    print("datos incorrectos")
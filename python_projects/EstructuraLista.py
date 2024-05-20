





users = []

user1 = [1017931639, "Jose", "Velasquez", 3193416857, "jv@mail.com", "M", 16, "0208"]
user2 = [1017931638, "Sebastian", "Torres", 319341686, "sp@mail.com", "F", 17, "0207"]
user3 = [1017931637, "Emmanuel", "Carmona", 3193416859, "em@mail.com", "M", 18, "0200"]

users.append(user1)
users.append(user2)
users.append(user3)


for item in users:
    print(item)
    
print(users[1][4])

# crear inicio de sesion comparando el valor del correo y contraseña ingresado 
# por el usuario vs el que esta en la base de datos

def login(email, password):
    for user in users:
        if user[4] == email and user[7] == password:
            return True
    return False


email_input = input("ingresa tu correo o email: ")
password_input = input("ingresa tu contrasreña: ")

if login(email_input, password_input):
    print("ingresaste correctamente")
else:
    print("contraseña o correo incorrectos bro")




# las variables en python son de tipado dinamico
name = "Pepito"

# Notacion snake
last_name = "Perez"
mail = "pepito@gmail.com"
salary = 1300000
state = True
note = 4.5
gender = 'm'

print(mail)

# Hablemos de concatenacion usando +

print("Nombre: " + name)

# Hablemos de concatenacion usando ,

print("correo",mail)

# hablemos de concatenacion format

print(f"Nombre {name}\n Apellido {last_name}\n Correo {mail}\n Salario {salary}\n " )

#type me permite conocer de que tipo es una variable

print(type(salary))

# Como capturar datos desde la consola input()

phone = input("Telefono: ")

print(f"Telefono:{phone}")

aux_transporte = int(input("Ingrese el aux de transporte"))

total_salary = salary + aux_transporte

print(f"El salario total es {total_salary}")

per_loan_discount = 0.3

loan_discount = salary * per_loan_discount

total_salary = salary + aux_transporte - loan_discount

print (f"El salario total es {total_salary}\nDescuentos:\nPrestamos:{loan_discount}")

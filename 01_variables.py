#Variables

my_variable = "My String variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False

print(my_variable, my_int_variable, my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#Concatenacion de variables en un print
print(my_variable, my_int_to_str_variable,my_bool_variable)
print("Este es el valor de:",my_bool_variable)

#Funciones del sistema
print(len(my_int_to_str_variable))

#Variables en una sola linea !cuidado con abusar de esta sintaxis
name, surname, alias, age = "Carlos", "Gonzalez", "elunico567", 33
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

#Inputs
'''
name = input('Cual es tu nombre ')
age = input("Cuantos anos tienes ")

print(name)
print(age)
'''
#Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

#Forzamos el tipo
address : str = "Mi direccion"
address = 32
print(address)
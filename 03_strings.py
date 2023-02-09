### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
# len() saber cuantos caracteres consumio el string


print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)  #concatenar

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)    #tabulacion

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo
print("-" * 50)
name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #las llaves entras las variables
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) # los "%" es llamar las variables como turbo C
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) #metodo tradicional llamar las variables
print(f"Mi nombre es {name} {surname} y mi edad es {age}")  #con llaves y las variables

print("-" * 50)

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)

print("-" * 50)
# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

print("-" * 50)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
'''
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo
'''
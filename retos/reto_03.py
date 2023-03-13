#Reto #3: EL GENERADOR DE CONTRASEÑAS
# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */
import random
import string

def passwordGeneration(password_type):

    letters = string.ascii_uppercase
    symbols = "!@#$%^&*()_+-={}[]|\:;\"'<>,.?/~`"
    range_string = 0
    range_numeric = 0
    range_symbol = 0

    password_len = int(input("¿De cuantos caracteres deseas tu contraseña? Digita (8 o 16): "))

    # if password_len == 8:
    #     if password_type == 1:
    #         range_string = 4
    #         range_numeric = 2
    #         range_symbol = 2
    #     elif password_type == 2:
    #         range_string = 4
    #         range_numeric = 4
    #         range_symbol = 0
    #     elif password_type == 3:
    #         range_string = 4
    #         range_numeric = 0
    #         range_symbol = 4
    #     elif password_type == 4:
    #         range_string = 0
    #         range_numeric = 4
    #         range_symbol = 4
    #     elif password_type == 5:
    #         range_string = 8
    #         range_numeric = 0
    #         range_symbol = 0
    #     elif password_type == 6:
    #         range_string = 0
    #         range_numeric = 8
    #         range_symbol = 0
    #     elif password_type == 7:
    #         range_string = 0
    #         range_numeric = 0
    #         range_symbol = 8

    range_dict = {
        (8, 1): (4, 2, 2),
        (8, 2): (4, 4, 0),
        (8, 3): (4, 0, 4),
        (8, 4): (0, 4, 4),
        (8, 5): (8, 0, 0),
        (8, 6): (0, 8, 0),
        (8, 7): (0, 0, 8),
        (16, 1): (8, 4, 4),
        (16, 2): (8, 8, 0),
        (16, 3): (8, 0, 8),
        (16, 4): (0, 8, 8),
        (16, 5): (16, 0, 0),
        (16, 6): (0, 16, 0),
        (16, 7): (0, 0, 16),
    }
    range_string, range_numeric, range_symbol = range_dict[(password_len, password_type)]


    random_string = ''.join([random.choice(letters) for _ in range(range_string)])    
    random_numeric = ''.join([str(random.randint(0, 9)) for _ in range(range_numeric)])
    random_symbol = ''.join([random.choice(symbols) for _ in range(range_symbol)])
    password = random_string + random_numeric + random_symbol

    print(password)






def password_type():

    password_type = 0
    upper_case = False
    numeric_case = False
    symbol_case = False

    print("Hola, este es tu generador de contraseñas", end="\n")
    password_upper = input("¿Quieres que incluya letras mayúsculas?: (Y/N): ")
    password_numeric = input("¿Quieres que incluya números?: (Y/N): ")
    password_symbol = input("¿Quieres que incluya símbolos?: (Y/N): ")

    if password_upper == 'Y':
        upper_case = True
    else:
        upper_case = False
    
    if password_numeric == 'Y':
        numeric_case = True
    else:
        numeric_case = False

    if password_symbol == 'Y':
        symbol_case = True
    else:
        symbol_case = False

    if upper_case and password_numeric and symbol_case:
        password_type = 1
        print("type 1")
    elif upper_case and numeric_case:
        password_type = 2
        print("type 2")
    elif upper_case and symbol_case:
        password_type = 3
        print("type 3")
    elif numeric_case and symbol_case:
        password_type = 4
        print("type 4")
    elif upper_case:
        print("type 5")
        password_type = 5
    elif numeric_case:
        print("type 6")
        password_type = 6
    elif symbol_case:
        print("type 7")
        password_type = 7
    else:
        print("tu contraseña solo tendrá letras minúsculas")
        password_type = 8

    return password_type


password_type = password_type()
passwordGeneration(password_type)
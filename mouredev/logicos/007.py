#/*
# * Crea un programa que invierta el orden de una cadena de texto
# * sin usar funciones propias del lenguaje que lo hagan de forma automática.
# * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
# */

def invert_me(par: str):
    my_return = []
    counter = -1
    for g in range(len(par)):
        my_return.append(par[counter])
        counter += -1

    print("".join(my_return))
    

invert_me("hola mundo")

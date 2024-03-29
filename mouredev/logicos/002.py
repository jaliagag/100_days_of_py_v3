#/*
# * Escribe una función que reciba dos palabras (String) y retorne
# * verdadero o falso (Bool) según sean o no anagramas.
# * - Un Anagrama consiste en formar una palabra reordenando TODAS
# *   las letras de otra palabra inicial.
# * - NO hace falta comprobar que ambas palabras existan.
# * - Dos palabras exactamente iguales no son anagrama.
# */


def myfunc(a: str, b: str):
    primera = list(a)
    segunda = list(b)
    pr_dict = {}
    pr_sec = {}
    if len(primera) == len(segunda):
        for i in primera:
            if i in pr_dict.keys():
                pr_dict[i] =+ 1
            else:
                pr_dict[i] = 1
        
        for i in segunda:
            if i in pr_sec.keys():
                pr_sec[i] =+ 1
            else:
                pr_sec[i] = 1

        for i in pr_dict.keys():
            if i in pr_sec.keys():
                if pr_dict[i] == pr_sec[i]:
                    continue
            else:
                return False

    return True

print(myfunc("hola","olah"))

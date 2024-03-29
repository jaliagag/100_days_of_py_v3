#/*
# * Escribe un programa que se encargue de comprobar si un número es o no primo.
# * Hecho esto, imprime los números primos entre 1 y 100.
# */


def primo(a: int):
    if a in [1,2,3,5,7]:
        return True
    elif a % 2 == 0 \
        or a % 3 == 0\
        or a % 5 == 0\
        or a % 7 == 0:
        return False
    else:
        return True


for i in range(1,51):
    print(i,primo(i))

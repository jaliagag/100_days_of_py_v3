#/*
# * Escribe un programa que imprima los 50 primeros números de la sucesión
# * de Fibonacci empezando en 0.
# * - La serie Fibonacci se compone por una sucesión de números en
# *   la que el siguiente siempre es la suma de los dos anteriores.
# *   0, 1, 1, 2, 3, 5, 8, 13...
# */

def fibo(a: int, b: int):
    return a + b

start = 0
increment = 1
answer = 0

print(start)
print(increment)

for i in range(1,51):
    answer = fibo(start, increment)
    start = increment
    increment = answer

    print(answer)
    #print(f"\t{start}\t {increment}")





#/*
# * Crea una única función (importante que sólo sea una) que sea capaz
# * de calcular y retornar el área de un polígono.
# * - La función recibirá por parámetro sólo UN polígono a la vez.
# * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# * - Imprime el cálculo del área de un polígono de cada tipo.
# */

def area(poligono: str, data1: int, data2: int):
    lowerme = poligono.lower()
    if lowerme == "triangulo":
        base = data1
        height = data2
        return (data1 * data2) * 0.5

    elif lowerme == "cuadrado":
        lado = data1
        lado2 = data2
        if lado != lado2:
            print("No es un cuadrado! es un rectangulo - para que sea un cuadrado, ambos datos/lados deben ser iguales")
            return False
        return lado * lado2

    elif lowerme == "rectangulo":
        length = data1
        width = data2
        return data1 * data2

    else:
        return False

print(area("cuadrado", 2,2))
print(area("cuadrado", 2,3))
print(area("triangulo", 20,10))
print(area("rectangulo", 4,2))
print(area("cualca", 4,2))

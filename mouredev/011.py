# EJERCICIO:
# Desarrolla un programa capaz de crear un archivo que se llame como
# tu usuario de GitHub y tenga la extensión .txt.
# Añade varias líneas en ese fichero:
# - Tu nombre.
# - Edad.
# - Lenguaje de programación favorito.
# Imprime el contenido.
# Borra el fichero.
#
# DIFICULTAD EXTRA (opcional):
# Desarrolla un programa de gestión de ventas que almacena sus datos en un 
# archivo .txt.
# - Cada producto se guarda en una línea del arhivo de la siguiente manera:
#   [nombre_producto], [cantidad_vendida], [precio].
# - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#   actualizar, eliminar productos y salir.
# - También debe poseer opciones para calcular la venta total y por producto.
# - La opción salir borra el .txt.

import requests
import os
import re

TOKEN = os.environ["GHPPT"]

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {TOKEN}"})

def get_user():
    return session.get("https://api.github.com/user").json()["login"]

def write_to_file(filename: str, data: list):
    f = open(f"{filename}.txt", "a")
    f.write(f"{data[0]}, {data[1]}, {data[2]}\n")
    f.close()

def load_product(filename: str):
    product_name = input("Nombre del producto: ")
    q_sold = input("Cantidad vendida: ")
    price= input("Precio: ")
    return [product_name, q_sold, price]


def create_file(filename: str):
    f = open(f"{filename}.txt", "a")
    f.close()
    #    name = input("Ingrese su nombre: ")
    #    age = int(input("Ingrese su edad: "))
    #    pr_lang = input("Cual es su lenguaje de programación favorito? ")
    #
    #    f.write(f"- Tu nombre: {name}\n")
    #    f.write(f"- Tu edad: {age}\n")
    #    f.write(f"- Lenguaje de programación favorito: {pr_lang}\n")
    #


def read_file(filename: str):
    f = open(f"{filename}.txt","r")
    print(f.read())
    f.close()

def delete_file(filename: str):
    try: 
        os.remove(f"{filename}.txt")
        print(f"File '{filename}' deleted successfully.")

    except FileNotFoundError: print(f"File '{filename}.txt' not found.")


def describe(filename: str):
    product = input("Ingrese el nombre del producto: ")

    f = open(f"{filename}.txt", "r")

    for i in f.readlines():
        if product in i.split(",")[0]:
            print(i, end="")
            return True
    print(f"product `{product}` was not found")
    f.close()
    return False

def update_product(filename: str):
    read_file(filename) # muestro el archivo completo
    product = input("Ingrese el nombre del producto a modificar: ")

    f = open(f"{filename}.txt","r+")

    for i in f:
        if product in i.split(",")[0]:

            print("Ingrese nuevos valores del producto")
            product = load_product(filename)
            to_string = ', '.join(product)

            f.write(re.sub(f"^{i}",to_string,i))

            f.close()
            return True


    print(f"product `{product}` was not found")
    f.close()
    return False

menu = """
1) Cargar productos
2) Ver productos
3) Ver producto especifico
4) Modificar productos
5) Ver totales de venta

9) Ver el menu
0) Salir
"""
if __name__ == "__main__":
    username = get_user()
    create_file(username)
    print(menu)
    while True:
        try:
            option = int(input("Que desea hacer? "))
            if option == 1:
                product = load_product(username)
                print(product)
                write_to_file(username, product)
            elif option == 2:
                read_file(username)
            elif option == 3:
                describe(username)
            elif option == 4:
                update_product(username)
            elif option == 9:
                print(menu)
            elif option == 0:
                delete_file(username)
                exit()
        except ValueError:
            print("Ingrese solo numeros enteros")
        except KeyboardInterrupt:
            print("\nSaliendo...")
            exit()




    #create_file(username)
    #delete_file(username)


    #    curl -L \
    #      -H "Accept: application/vnd.github+json" \
    #      -H "Authorization: Bearer <YOUR-TOKEN>" \
    #      -H "X-GitHub-Api-Version: 2022-11-28" \
    #      https://api.github.com/user

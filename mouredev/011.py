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

TOKEN = os.environ["GHPPT"]

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {TOKEN}"})

def get_user():
    return session.get("https://api.github.com/user").json()["login"]

def create_file(filename: str):
    f = open(f"{filename}.txt", "w")
    name = input("Ingrese su nombre: ")
    age = int(input("Ingrese su edad: "))
    pr_lang = input("Cual es su lenguaje de programación favorito? ")

    f.write(f"- Tu nombre: {name}\n")
    f.write(f"- Tu edad: {age}\n")
    f.write(f"- Lenguaje de programación favorito: {pr_lang}\n")


def read_file(filename: str):
    f = open(f"{filename}.txt","r")
    print(f.read())

def delete_file(filename: str):
    try: 
        os.remove(f"{filename}.txt")
        print(f"File '{filename}' deleted successfully.")

    except FileNotFoundError: print(f"File '{filename}.txt' not found.")

if __name__ == "__main__":
    username = get_user()
    create_file(username)
    read_file(username)
    delete_file(username)


    #    curl -L \
    #      -H "Accept: application/vnd.github+json" \
    #      -H "Authorization: Bearer <YOUR-TOKEN>" \
    #      -H "X-GitHub-Api-Version: 2022-11-28" \
    #      https://api.github.com/user

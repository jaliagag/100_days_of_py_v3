import funciones as f
from db.models.tarea import Tarea
from db.client import client
from datetime import datetime
from tabulate import tabulate

now = datetime.now()

def ver_tareas(info):
    data = []
    for i in info:
        data.append([i["titulo"],i["fecha_creacion"],i["fecha_limite"],i["description"]])
    col_names = ["Tarea", "Fecha creacion", "Fecha limite", "Descripcion"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))

def crear_tarea(date: str):
    titulo = input("\n\tTitulo de la tarea: " or "<blank>")
    description = input("\tDescripcion de la tarea: " or "<blank>")
    fecha_creacion = date
    fecha_limite = input("\tFecha de finalizacion: " or "<blank>")

    tarea = {
        "titulo": titulo,
        "description": description,
        "fecha_creacion": fecha_creacion,
        "fecha_limite": fecha_limite,
        "estado": True
    }

    client.tareas_app.tareas.insert_one(tarea)

def eliminar_tarea():
    print("Estas son las tareas: ")
    ver_tareas(client.tareas_app.tareas.find())
    deleme = input()
    client.tareas_app.tareas.find_one_and_delete()

# menu de opciones
print(f"\nGestor de tareas NotPip - {now.strftime("%d-%m-%Y")}")
while True:
    print("""
    1. Generar tarea
    2. Ver tareas
    3. Marcar tarea como completa
    4. Editar tarea
    5. Salir
    """)

    opcion = input("Elija una opcion:\n")

    match opcion:
        case "1":
            crear_tarea(now.strftime("%d-%m-%Y"))
        case "2":
            ver_tareas(client.tareas_app.tareas.find())
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Hasta la proxima!")
            exit()
        case _:
            pass

client.close()

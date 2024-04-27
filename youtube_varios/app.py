import funciones as f
from db.models.tarea import Tarea
from db.client import client
from datetime import datetime
from tabulate import tabulate


database = client["tareas_app"]
collection = database["tareas"]
datos = collection.find()


#async def create_user(user: User):
#
#    if type(search_user("email", user.email)) == User:
#        raise HTTPException(
#        status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
#
#    user_dict = dict(user)
#    del user_dict["id"]
#
#    id = db_client.users.insert_one(user_dict).inserted_id
#
#    new_user = user_schema(db_client.users.find_one({"_id": id}))
#
#    return User(**new_user) # ** para indicar que le paso todos los campos

def ver_tareas(info):
    data = []
    for i in info:
        data.append([i["titulo"],i["fecha_creacion"],i["fecha_limite"]])
    col_names = ["Tarea", "Fecha creacion", "Fecha limite"]
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
        "fecha_limite": fecha_limite
    }

    collection.insert_one(tarea)

    return

now = datetime.now()
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

    opcion = input("Elija una opcion: ")

    match opcion:
        case "1":
            crear_tarea(now.strftime("%d-%m-%Y"))
        case "2":
            ver_tareas(datos)
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case _:
            pass

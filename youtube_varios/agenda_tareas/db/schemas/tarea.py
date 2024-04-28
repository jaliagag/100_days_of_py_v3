def tarea_schema(tarea) -> dict:
    return {
        "id": str(tarea["_id"]),
        "titulo": tarea["titulo"],
        "descripcion": tarea["descripcion"],
        "fecha_creacion": tarea["fecha_creacion"],
        "fecha_limite": tarea["fecha_limite"],
        "estado": tarea["estado"]
    }


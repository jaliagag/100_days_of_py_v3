from pydantic import BaseModel
from typing import Optional

class Tarea(BaseModel):
    #id: Optional[str] #str | None # es opcional; en mongodb, id son strings para que puedan ser mas largos
    id: str = None
    titulo: str
    descripcion: str
    fecha_creacion: str
    fecha_limite: str
    estado: bool

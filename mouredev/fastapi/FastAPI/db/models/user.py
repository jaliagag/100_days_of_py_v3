from pydantic import BaseModel

class User(BaseModel):
    id: str | None # es opcional; en mongodb, id son strings para que puedan ser mas largos
    username: str
    email: str

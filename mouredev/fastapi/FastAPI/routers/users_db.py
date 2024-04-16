from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema
from db.client import db_client


from fastapi.responses import FileResponse

router = APIRouter(
                prefix="/userdb",
                tags=["userdb"],
                responses={status.HTTP_404_NOT_FOUND: {"message": "no encontrado"}}
                )

# uvicorn users:router --reload

@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)



user_list = []


@router.get("/")
async def users():
    return user_list

@router.get("/{id}")
async def user(id: int): # query
    return search_user(id)

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.local.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.local.find_one({"_id": id}))

    return User(**new_user) # ** para indicar que le paso todos los campos 


@router.put("/")
async def update_user(user: User):
    for index, existing_user in enumerate(user_list):
        if existing_user.id == user.id:
            user_list[index] = user
            return {"status": f"OK - user {user.name} successfully updated","user": user}

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/{id}")
async def delete_user(id: int):
    for index, existing_id in enumerate(user_list):
        if existing_id.id == id:
            del user_list[index]
            return {"status": f"OK - user successfully deleted"}

    return {"error": "user not found"}


def search_user(id:int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"error": "list index out of range"}


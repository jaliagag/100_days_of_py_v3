from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client


router = APIRouter(
                prefix="/userdb",
                tags=["userdb"],
                responses={status.HTTP_404_NOT_FOUND: {"message": "no encontrado"}}
                )

user_list = []

@router.get("/", response_model=list[User])
async def users():
    return db_client.local.users.find()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):

    if type(search_user("email", user.email)) == User:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.local.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.local.users.find_one({"_id": id}))

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


def search_user(field: str, key):

    try:
        user = db_client.local.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}


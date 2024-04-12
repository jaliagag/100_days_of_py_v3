from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

#app = APIrouter(prefix="/basicauth", 
#                   tags=["jwtauth"], # para la documentacion
#                   responses={ 404: { "message": "not found" } }
#                   )

ALGORITHM = "HS256"

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")
crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "conan": {
        "username": "conan",
        "fullname": "conan aliaga",
        "email": "conan@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "paula": {
        "username": "paula",
        "fullname": "paula centanni",
        "email": "pmcentanni@gmail.com",
        "disabled": False,
        "password": "amorcis"
    },
    "jose": {
        "username": "jose",
        "fullname": "jose aliaga",
        "email": "jmfaliaga@gmail.com",
        "disabled": False,
        "password": "noselaverad1234"
    },
    "simba": {
        "username": "simba",
        "fullname": "simba centanni",
        "email": "apestoso@gmail.com",
        "disabled": True,
        "password": "lloroporqueconanesmejor"
    },
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

#def search_user(username: str):
#    if username in users_db:
#        return User(**users_db[username])
#
## criterio de dependencia
#async def current_user(token: str = Depends(oauth2)):
#    user = search_user(token)
#    if not user:
#        raise HTTPException(
#            status_code=status.HTTP_401_UNAUTHORIZED, 
#            detail="usuario no autorizado", 
#            headers={"WWW-Authenticate": "Bearer"}
#        )
#    if user.disabled:
#        raise HTTPException(
#            status_code=status.HTTP_400_BAD_REQUEST, 
#            detail="usuario inactivo")
#
#    return user
#
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="usuario incorrecto")

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="password incorrecta")


    return {"access_token": user.username , "token_type": "bearer"}
#
#@app.get("/users/me")
#async def me(user: User = Depends(current_user)):
#    return user
#
#
#

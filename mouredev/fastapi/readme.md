# FASTAPI

### type hints

declaramos el tipo de una variable

`my_var: str = "hola mundo"`

es un tipado _suave_. 

### instalacion

servidor local de fastapi: `uvicorn`.

```sh
pip install "fastapi[all]"
```

### async

una funcion sincrona hace que cuando hacemos una llamada, la api no puede hacer nada hasta que reciba respuesta del servidor.

la mayoria de las funciones que usaremos van a ser asincronas.

```py
@app.get("/")
async def root():
  return "holis"
```

### uvicorn

`uvicorn main:app --reload`

### documentacion

`localhost:8000/docs`
`localhost:8000/redoc`

## path vs dynamic

- solemos usar path, o sea `users/1` cuando consideramos que es un parametro obligatorio, fijo; la url puede ser algo dinamico.
- solemos usar query para los parametros que pueden no ser necesarios para hacer una peticion. por ejemplo, al hacer una peticion a una db. forma parte de la query la paginacion, decirle a la API "dame las publicaciones del usuario X de la 1 a la 10"; cuando estamos por la publicacion 7 (ponele), le pedimos a la API que nos de los 10 siguientes. es algo variable, que puede ir o no ir.

el `?` solo va en el primer parametro del query string; despues, para concatenar, usamos `&`

## status codes

cuando lanzamos un error, usamos `raise`:

```py
@app.post("/user/", status_code=201) # << codigo de respuesta por defecto, se declara en la cabecera
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="user already exists")
    else:
        user_list.append(user)
        return {"status": "OK - user successfully added"}
```

`raise` lo que hace es "propagar" la excepcion.

Para que lo que se devuelva no sea un sucio string, tenemos que usar `response_model`: `@router.post("/", response_model=User, status_code=201)`. esto, en swagger se vera que lo que devuelve el status code del post de los usuarios, no es un string, si no un json.

## recursos estaticos

acceder a imagenes, pdfs... 

```py
from fastapi.staticfiles import StaticFiles
...
app.mount("/static", StaticFiles(directory="static"), name="static")

```

## basic auth

llamada /users/me --> devuelve 401, no autenticado
primero hay que obtener un token, con un post a /login con un form 


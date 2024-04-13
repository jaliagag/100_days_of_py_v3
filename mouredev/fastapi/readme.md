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

## depends

- [link1 - Depends](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [link2 - security](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)

> Annotated in python allows developers to declare the type of a reference and provide additional information related to it.
> 
> `name = Annotated[str, "first letter is capital"]`
> 
> This tells that `name` is of type str and that name[0] is a capital letter.
> 
> On its own Annotated does not do anything other than assigning extra information (metadata) to a reference. It is up to another code, which can be a library, framework or your own code, to interpret the metadata and make use of it.
> 
> For example, FastAPI uses Annotated for data validation:
> 
> `def read_items(q: Annotated[str, Query(max_length=50)])`
> 
> Here the parameter q is of type str with a maximum length of 50. This information was communicated to FastAPI (or any other underlying library) using the Annotated keyword.

Para ver la informacion de `users/me`, dependo de `current_user` que depende de `oauth2`. pasos para acceder a `users/me`:

- ir a `/login` - esto nos da un diccionario con un token
- vamos a `/users/me`:
  - este usa `current/user` y le pasa un token 

## jwt auth

Generar contrasena random: `openssl rand -hex 32` 

Hay un error que parece estar contenido:

```sh
(trapped) error reading bcrypt version
Traceback (most recent call last):
  File "/Users/josemanuelfranciscoaliaga/Documents/myprojects/100_days_of_py_v3/mouredev/fastapi/virtual-fapi/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 620, in _load_backend_mixin
    version = _bcrypt.__about__.__version__
              ^^^^^^^^^^^^^^^^^
AttributeError: module 'bcrypt' has no attribute '__about__'
```

Al parecer, [la solucion](https://github.com/pyca/bcrypt/issues/684#issuecomment-1836872510) es usar `bcrypt==4.0.1`

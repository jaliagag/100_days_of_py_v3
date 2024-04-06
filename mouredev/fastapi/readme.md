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


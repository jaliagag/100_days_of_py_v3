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


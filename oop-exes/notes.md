# Classes

- Atributos de clase: son heredados por todas las instancias de las clases que se creen (por ejemplo, especie). son comunes a todas las instancias de las clases.
- Atributos de instancia: cada instancia que se cree tiene que tener esos atributos creados para que este completa - son unicos a la instancia que creamos (por ejemplo nombre)
- `self`: hace referencia a la instancia de la clases
- metodos: las acciones que puede hacer la clase
- constructor: `__init__` crea cada una de las instancias (o sea, cuando creamos `paula = Persona(atributos)` estamos llamanod al constructor __init__ y tenemos que pasarle los atributos declarados en el constructor)
- `__getitem__`: si se desea que los usuarios puedan leer los elementos mediante el uso de corchetes es necesario implementar el método `__getitem__` en la clase. Este elemento necesita un parámetro adicional, que es la posición del elemento a leer. La función debe retornar el valor leído.
- `__setitem__`: para modificar un valor; es necesario pasar dos parámetros adicionales, la posición y el valor a reemplazar
- `__iter__`: hace que nuestra clase sea iterable, lo que permite usarla por ejemplo en bucles tipo for, es necesario implementar este método. En el ejemplo devuelve una cadena con el índice y el valor de cada elemento

```py
class Vector():
  def __init__(self, data):
    self._data = data
  def __getitem__(self,pos):
    return self._data[pos]
  def __setitem__: (self, pos, value):
    return self._data[pos] = value
  def __iter__(self):
    for pos in range(0, len(self._data)):
      yield f"Value[{pos}]: {self._data[pos]}"
```

## Relaciones entre clases

```py
class Perro:
  def __init__(self, nombre: str):
    self.nombre = nombre

  def __str__(self):
    return self.nombre

class Persona:
  def __init__(self, nombre: str, perro: str):
    self.nombre = nombre
    self.perro = perro

  def __str__(self):
    return f"{self.nombre}: {self.perro}"

obama = Perro("obama")
jose = Persona("Jose",obama)

print(jose)
```



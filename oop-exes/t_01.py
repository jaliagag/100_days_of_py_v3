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


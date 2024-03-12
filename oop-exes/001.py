# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter. 

class Perro:
    # atributos de clase
    especie = "mamifero"

    def __init__(self,nombre: str,raza: str): # constructor - Es una variable que representa la instancia de la clase, y deberá estar siempre ahí.

        # atributos de la instancia
        self.nombre = nombre
        self.raza = raza

    # metodos
    def ladrar(self): # hace referencia a la instancia de la clase - no tiene argumentos
        print("Guau")

    def caminar(self, pasos: int):
        print(f"{self.nombre} da {pasos} pasos")


#obama = Perro("Obama","negro") # entre los parentesis usamos atributos de la instancia que creamos que se llama uno
#conan = Perro("Conan","marron")

#print(obama.nombre)
#print(obama.raza)
#obama.ladrar()
#obama.caminar(4)

class Persona:
    especie = "humano"

    def __init__(self, name: str, age: int, sex: str, status: str, professional: bool):
        self.name = name
        self.age = age
        self.sex = sex
        self.status = status
        self.professional = professional

    def __str__(self):
        return f"Characteristics of the person: \n\tname: {self.name}, \n\tage: {self.age}, \n\tsex: {self.sex}, \n\tstatus: {self.status}, \n\tprofessional: {self.professional}"

    def saludar(self,saludo: str):
        print(f"{self.name} dice {saludo}")

jose = Persona("Jose", 34, "male", "alive",True)
jose.saludar("adios")
print(jose)








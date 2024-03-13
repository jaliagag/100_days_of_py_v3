class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

class Perro(Animal):
    def __init__(self,especie, edad, owner):
        super().__init__(especie, edad)
        self.owner = owner

conan = Perro('mamifero', '1', 'jose')
print(conan.especie, conan.edad, conan.owner)

# https://github.com/jaliagag/22_coderhouse_python_jaliaga/blob/master/clase13/atleta.py

class Atleta:

    def __init__(self, name: str, last_name: str, height: float, weight: float, phone: str):
        self.__name = name
        self.__last_name = last_name
        self.__height = height
        self.__weight = weight
        self.__phone = phone
        self.__bodyMassIndex = round(weight / (height * height ), 2)

        #def __str__(self):
        #    return f"{self.__name} {self.__last_name} {self.__bodyMassIndex}"

jose = Atleta(name="Jose",last_name="Aliaga",height=1.91,weight=90.0,phone="1234")
print(jose)

class Car:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.saludar()

        #Private data
        __model = "ddd"

    #Metodo de instancia
    def saludar(self):
        print (f"hola {self.name}")

kia = Car("pedro", "34")
print(kia.age)
#kia.saludar()



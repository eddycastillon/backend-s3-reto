#Clase persona
class Persona:
    def __init__(self, nombre="", edad=""):
        self.nombre = nombre
        self.edad = edad

class Archivo:
    def __init__(self, nombre):
        self.nombre_archivo = nombre

    def mostrar(self):
        try:
            archivo = open(self.nombre_archivo, "r")
            for linea in archivo.readlines():
                print(linea.rstrip())
            archivo.close
        except Exception as e:
            print (e)
    

    def agregar(self, objeto):
        try:
            archivo = open(self.nombre_archivo, "a")
            nombre = objeto.nombre
            edad = objeto.edad
            archivo.write(f"{nombre}, {edad}\n")
            archivo.close()
        except Exception as e:
            print (e)
    

carlos = Persona("Carlos", 30)
valeria = Persona("Valeria", 25)
archivo = Archivo("personas.txt")
archivo.agregar(carlos)
archivo.agregar(valeria)
archivo.mostrar()
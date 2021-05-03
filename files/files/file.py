file = open("prueba", "w")
file.write("Hello world")
file.close()

#Read file
while True:
    try:
        archivo = open("prueba", "r")
        archivo.close()
        print("Se abrio el archivo")
        break
    except FileNotFoundError as e:
        create = open("prueba", "w")
        create.close()
        print("Se creo el archivo")
    #except Exception as e:
    #    print(e.__class__.__name__)
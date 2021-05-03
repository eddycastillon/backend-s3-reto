try:
    archivo = open("prueba", "r")
    for line in archivo.readlines():
        print(line)
    archivo.close()
except Exception as e:
    print(e.__class__.__name__) 
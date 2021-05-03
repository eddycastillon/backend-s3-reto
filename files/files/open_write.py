try:
    archivo = open("prueba", "a")
    for i in range(20,25):
        archivo.write(f"Linea {i}\n")

    archivo.close()
except Exception as e:
    print(e)
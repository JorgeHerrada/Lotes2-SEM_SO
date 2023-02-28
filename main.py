from carpeta import Carpeta

if __name__ == '__main__':

    # original = input('Introduce el nombre de la carpeta origen: ')
    original = ".\carpetaOriginal"
    # destino = input('Introduce el nombre de la carpeta destino: ')
    destino = ".\carpetaMamalona"

    # Inicialización
    carpeta = Carpeta(original, destino)

    # movemos archivos/carpetas 
    carpeta.mover()

    # entramos a la carpeta y modificamos el texto
    carpeta.iterar(carpeta.dirDestino)
    

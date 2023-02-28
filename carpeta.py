import os
from distutils.dir_util import copy_tree
from random import randint


class Carpeta:
    dirOriginal = ""
    dirDestino = ""

    # Constructor
    def __init__(self, dirOriginal, dirDestino) -> None:
        self.dirOriginal = dirOriginal
        self.dirDestino = dirDestino

    # Copia contenido de carpeta original a destino
    def mover(self):
        copy_tree(self.dirOriginal, self.dirDestino)

    # cambia caracteres a-z por numero random y
    # numeros por caracteres random
    def swapChars(self, texto) -> str:
        salida = ""

        for i in range(len(texto)):
            if texto[i].isnumeric():
                salida += chr(randint(65, 90))
            elif texto[i].isalpha():
                salida += chr(randint(48, 57))
            else:  # no 0-9, a-z o A-Z
                salida += texto[i]

        return salida

    def iterar(self, path=None):

        try:
            with os.scandir(path) as ficheros:
                for fichero in ficheros:
                    if fichero.is_file():
                        original = open(fichero.path, "r")
                        # nuevo = open("temp.txt","w")

                        lineas = original.readlines()
                        original.close()
                        original = open(fichero.path, "w")

                        nuevaLinea = ""
                        for linea in lineas:
                            nuevaLinea = self.swapChars(linea)
                            original.write(nuevaLinea)

                        original.close()
                        # copiamos
                    elif fichero.is_dir():
                        self.iterar(fichero.path)
        except:
            print("Error")

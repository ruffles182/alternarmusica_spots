# -*- coding: utf-8 -*-
from os import listdir
from os import rename
import os
import shutil
import random 

# Clase principal
class AcomodoCanciones:
    dirMus = "Música Joinet/"
    nuevoDir = "testNuevo/"
    separadorSpot = " ---- "
    maxCaracteres = 30
    lista = []
    cantidadSpots = 1
    enumerar = False

    def verificarOrigen(self):
        if os.path.exists(self.dirMus):
            return True
        else:
            return False
    def verificarDestino(self):
        if os.path.exists(self.nuevoDir):
            return True
        else:
            return False
    def crearDestino(self):
        if not os.path.exists(self.nuevoDir):
            os.makedirs(self.nuevoDir)

# variables globales
separador = "----------------------------------------------------------------------"
salir = False
playlist = AcomodoCanciones()

# Funciones
def cambiarDirdest():
    respNewDir = input("nombre de la carpeta destino (debe estár vacia): ")
    playlist.nuevoDir = respNewDir + "/"
def cambiarDirorigen():
    respOrDir = input("nombre de la carpeta origen (no debe incluir carpetas): ")
    playlist.dirMus = respOrDir + "/"
def cambiarSeparador():
    playlist.separadorSpot = input("ingrese el nuevo separador: ")
def cambiarCaracteresMax():
    playlist.maxCaracteres = input("ingrese el máximo de caracteres: ")
def cambiarSpots():
    print(separador)
    playlist.cantidadSpots = int(input("ingrese la cantidad de spots: "))
    print(separador)
    n = 0
    while n < playlist.cantidadSpots:
        spotnombre = input("ingrese el nombre del spot " + str(n+1) + " (debe incluir el formato de archivo):")
        playlist.lista.append(spotnombre)
        n = n+1
def aleatorizar():
    listaCan = listdir(playlist.dirMus)
    random.shuffle(listaCan)
    n = 0
    for cancion in listaCan:
        nombrealeatorizado = str(f'{n:03}') + cancion
        rename(playlist.dirMus+cancion, playlist.dirMus + nombrealeatorizado)
        print(nombrealeatorizado)
        n = n + 1

def cambiarEnumerar():
    playlist.enumerar = not playlist.enumerar
def generar():
    if playlist.verificarOrigen():
        if not playlist.verificarDestino():
            playlist.crearDestino()

        print("generando lista en " + str(playlist.nuevoDir))
        spotActual = 1
        listaCan = listdir(playlist.dirMus)
        n = 0

        for cancion in listaCan:
            tamanioCadena = len(cancion)
            formato = cancion[tamanioCadena - 4 :]
            print(formato)
            enum = 0
            nombreCancion = cancion[:-4]
            caracteres = len(nombreCancion)
            caracteresSobrantes = caracteres - playlist.maxCaracteres

            if caracteresSobrantes > 1:
                nombreCancion = nombreCancion[:caracteres - caracteresSobrantes]

            nuevoNombre = (nombreCancion + formato)
            print(nuevoNombre)
            print(playlist.nuevoDir + nombreCancion + playlist.separadorSpot + playlist.lista[spotActual-1] + " --- " +str(spotActual))
            rename(playlist.dirMus+cancion, playlist.dirMus + nuevoNombre)
            if playlist.enumerar:
                shutil.copyfile(playlist.lista[spotActual-1], playlist.nuevoDir + str(f'{n:03}') + playlist.separadorSpot + playlist.lista[spotActual-1])
                n = n + 1
                shutil.copyfile(playlist.dirMus + nuevoNombre, playlist.nuevoDir + str(f'{n:03}') + formato)
                n = n + 1
            else :
                shutil.copyfile(playlist.lista[spotActual-1], playlist.nuevoDir + nombreCancion + playlist.separadorSpot + playlist.lista[spotActual-1])
                shutil.copyfile(playlist.dirMus + nuevoNombre, playlist.nuevoDir + nuevoNombre)
            if spotActual == len(playlist.lista):
                spotActual = 1
            else:
                spotActual = spotActual + 1

# interface
while not salir:
    enumerar = "Sí" if playlist.enumerar else "No"
    print(separador)
    print("Playlist Joinet")
    print(separador)
    print("1) Cambiar directorio destino - " + playlist.nuevoDir)
    print("2) Cambiar directorio inicial - " + playlist.dirMus)
    print("3) Cambiar separador - " + playlist.separadorSpot)
    print("4) Cambiar caracterres Máximos - " + str(playlist.maxCaracteres))
    print("5) Cambiar spots - " + str(playlist.cantidadSpots))
    print("6) Aleatorizar directorio Origen - no se puede deshacer")
    print("7) Cambiar enumerar (borrar el nombre) - " + enumerar)
    print("8) Generar")
    print("9) Salir")
    print(separador)

    opc = input("seleccione una opción: ")

    if (opc=="1"):
        cambiarDirdest()
    elif (opc=="2"):
        cambiarDirorigen()
    elif (opc=="3"):
        cambiarSeparador()
    elif (opc=="4"):
        cambiarCaracteresMax()
    elif (opc=="5"):
        cambiarSpots()
    elif (opc=="6"):
        aleatorizar()
    elif (opc=="7"):
        cambiarEnumerar()
    elif (opc=="8"):
        generar()
    elif (opc=="9"):
        salir = True
        break
        

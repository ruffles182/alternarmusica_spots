# -*- coding: utf-8 -*-

from os import listdir
from os import rename
import shutil

class acomodoCanciones:
    nuevoDir = "testNuevo/"
    dirMus = "Música Joinet/"
    separadorSpot = " ---- "
    maxCaracteres = 30
    lista = []
    cantidadSpots = 1
    enumerar = False

separador = "-------------------------------------------------------"
salir = False
playlist = acomodoCanciones()

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
def cambiarSeparador():
    playlist.separadorSpot = input("ingrese el nuevo separador: ")
def cambiarSpots():
    print(separador)
    playlist.cantidadSpots = int(input("ingrese la cantidad de spots: "))
    print(separador)
    n = 0
    while n < playlist.cantidadSpots:
        spotnombre = input("ingrese el nombre del spot " + str(n+1) + " (debe incluir el formato de archivo):")
        playlist.lista.append(spotnombre)
        n = n+1
def cambiarEnumerar():
    playlist.enumerar = not playlist.enumerar
def generar():
    print("generando lista en " + str(playlist.nuevoDir))
    print(playlist.lista[0] + " - " + playlist.lista[1])
    spotActual = 1
    listaCan = listdir(playlist.dirMus)
    for cancion in listaCan:
        nombreCancion = cancion[:-4]
        caracteres = len(nombreCancion)
        caracteresSobrantes = caracteres - playlist.maxCaracteres

        if caracteresSobrantes > 1:
            nombreCancion = nombreCancion[:caracteres - caracteresSobrantes]

        nuevoNombre = (nombreCancion + ".mp3")
        print(nuevoNombre)
        print(playlist.nuevoDir+nombreCancion+playlist.separadorSpot+playlist.lista[spotActual-1] + " --- " +str(spotActual))
        rename(playlist.dirMus+cancion, playlist.dirMus+nuevoNombre)
        shutil.copyfile(playlist.lista[spotActual-1], playlist.nuevoDir+nombreCancion+playlist.separadorSpot+playlist.lista[spotActual-1])
        shutil.copyfile(playlist.dirMus+nuevoNombre, playlist.nuevoDir+nuevoNombre)
        if spotActual == len(playlist.lista):
            spotActual = 1
        else:
            spotActual = spotActual + 1


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
    print("6) Cambiar enumerar - " + enumerar)
    print("7) Generar")
    print("8) Salir")
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
        cambiarEnumerar()
    elif (opc=="7"):
        generar()
    elif (opc=="8"):
        salir = True
        break
        

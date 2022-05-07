#!/usr/bin/python3
#configuracion.py
#Autor: Andrés Ripoll

import sys
import os
from subprocess import call

#Instala las imagenes de los routers
def instalar_imagenes():
	call("sudo chmod 666 /var/run/docker.sock", shell=True)
	call("docker pull ghcr.io/nokia/srlinux:latest", shell=True)
	call("docker import cEOS-lab-4.26.4M.tar.xz ceosimage:4.26.4M", shell=True)

	fin = open("./srlceos01.clab.yml", 'r') # in file
	fout = open("./srlceos01Tmp.clab.yml", 'w') # out file
	for line in fin:
		if "image: ceos:4.25.0F" in line:
			fout.write("        image: ceos:4.25.0F".replace("ceos:4.25.0F", "ceosimage:4.26.4M"))  #Cambiar por el nombre de la imagen que hayas descargado
		else:
			fout.write(line)
	fin.close()
	fout.close()
	call("sudo cat ./srlceos01Tmp.clab.yml > ./srlceos01.clab.yml", shell=True)
	call("sudo rm ./srlceos01Tmp.clab.yml", shell=True)

#Funcion para crear el lab de router cisco con arista
def crear_lab_ca():
	call("sudo containerlab deploy --topo csrceos01.clab.yml --reconfigure", shell=True)

#Funcion para crear el lab de router nokia con arista
def crear_lab_na():
	call("sudo containerlab deploy --topo srlceos01.clab.yml --reconfigure", shell=True)

#Prepara el entorno para el uso de netconf
def preparar_entorno():
	call("sudo docker cp ./startup-config clab-srlceos01-ceos:/mnt/flash/startup-config", shell=True)
	call(""" sudo docker exec -it clab-srlceos01-ceos Cli -p 15 -c "copy start run" """, shell=True)

#Funciones de ayuda
def mostrar_ayuda():
	ayuda_imagenes()
	print("")
	ayuda_lab_ca()
	print("")
	ayuda_lab_na()
	print("")
	ayuda_prepare()
	print("")
	print("help <cmd>             ---> para mostrar esta pantalla de ayuda o solo la ayuda de un comando.")
	print("\tParámetros:")
	print("\t\t<cmd> -> opcional: para mostrar la ayuda de un único comando.")

def ayuda_imagenes():
	print("imagenes                 ---> para instalar las imagenes de los routers del laboratorio. En concreto serán un router Nokia y el router Arista 4.26.4M.")

def ayuda_lab_ca():
	print("labca              ---> para crear el laboratorio de containerlab con un router Arista y uno de Cisco.")

def ayuda_lab_na():
	print("labna              ---> para crear el laboratorio de containerlab con un router Arista y uno de Nokia.")

def ayuda_prepare():
	print("prepare                  ---> para habilitar la configuración inicial con netconf en el router Arista.")

#Inicio del script

#Comprobamos que nos pasan más de dos argumentos
if len(sys.argv) < 2:
	print("Comandos disponibles:")
	print("")
	mostrar_ayuda()
	sys.exit()

#Ordenes
if sys.argv[1] == "imagenes":
	instalar_imagenes()
elif sys.argv[1] == "labca":
	crear_lab_ca()
elif sys.argv[1] == "labna":
	crear_lab_na()
elif sys.argv[1] == "prepare":
	preparar_entorno()
elif sys.argv[1] == "help":
	if len(sys.argv) > 2:
		if (sys.argv[2] == "imagenes"):
			ayuda_imagenes()
		elif (sys.argv[2] == "labca"):
			ayuda_lab_ca()
		elif (sys.argv[2] == "labna"):
			ayuda_lab_na()
		elif (sys.argv[2] == "prepare"):
			ayuda_prepare()
		else:
			mostrar_ayuda()
	else:
		mostrar_ayuda()

#Consola con datos
else:
	print("Orden no disponible.")
	print("Inténtelo de nuevo con alguno de estos comandos:")
	mostrar_ayuda()
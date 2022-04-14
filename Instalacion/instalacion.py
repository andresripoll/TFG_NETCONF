#!/usr/bin/python3
#instalacion.py
#Autor: Andrés Ripoll

import sys
import os
from subprocess import call

#Instala containerLab
def instalar_clab():
	call("sudo apt-get install", shell=True)
	call("sudo apt upgrade", shell=True)
	call("sudo apt install curl", shell=True)
	call(""" sudo bash -c "$(curl -sL https://get-clab.srlinux.dev)" """, shell=True)
	call("mkdir clab-quickstart", shell=True)
	os.chdir(os.getcwd() + "/clab-quickstart")
	call("cp -a /etc/containerlab/lab-examples/srlceos01/* .", shell=True)

#Instala ncclient
def instalar_ncclient():
	call("pip install ncclient", shell=True)

#Instala docker
def instalar_docker():
	call("sudo apt install docker.io", shell=True)

#Funciones de ayuda
def mostrar_ayuda():
	ayuda_clab()
	print("")
	ayuda_ncclient()
	print("")
	ayuda_docker()
	print("")
	print("help <cmd>               ---> para mostrar esta pantalla de ayuda o solo la ayuda de un comando.")
	print("\tParámetros:")
	print("\t\t<cmd> -> opcional: para mostrar la ayuda de un único comando.")

def ayuda_clab():
	print("containerlab             ---> para instalar containerlab.")

def ayuda_ncclient():
	print("ncclient                 ---> para instalar ncclient.")

def ayuda_docker():
	print("docker                   ---> para instalar docker.")

#Inicio del script

#Comprobamos que nos pasan más de dos argumentos
if len(sys.argv) < 2:
	print("Comandos disponibles:")
	print("")
	mostrar_ayuda()
	sys.exit()

#Ordenes
if sys.argv[1] == "containerlab":
	instalar_clab()
elif sys.argv[1] == "ncclient":
	instalar_ncclient()
elif sys.argv[1] == "docker":
	instalar_docker()
elif sys.argv[1] == "help":
	if len(sys.argv) > 2:
		if (sys.argv[2] == "containerlab"):
			ayuda_clab()
		elif (sys.argv[2] == "ncclient"):
			ayuda_ncclient()
		elif (sys.argv[2] == "docker"):
			ayuda_docker()
		else:
			mostrar_ayuda()
	else:
		mostrar_ayuda()

#Consola con datos
else:
	print("Orden no disponible.")
	print("Inténtelo de nuevo con alguno de estos comandos:")
	mostrar_ayuda()
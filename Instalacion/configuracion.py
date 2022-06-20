#!/usr/bin/python3
#configuracion.py
#Autor: Andrés Ripoll

import sys
import os
from subprocess import call

#Instala la imagen del router Arista y Nokia
def instalar_imagen_arista_nokia():
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
	call("sudo docker cp ./startup-config clab-csrceos01-ceos:/mnt/flash/startup-config", shell=True)
	call(""" sudo docker exec -it clab-csrceos01-ceos Cli -p 15 -c "copy start run" """, shell=True)

#Creación de la network entre telegraf y el router CSR1000v
def crear_network_1000v():
	call("sudo chmod 666 /var/run/docker.sock", shell=True)
	call("docker network create networkCSR1000v --subnet=172.21.0.0/16", shell=True)
	call("docker network connect --alias web1 networkCSR1000v dashboard_telegraf_1", shell=True)
	call("docker network connect --alias web2 networkCSR1000v clab-csrceos01-csr", shell=True)

#Borra el laboratorio
def destruir_lab():
	call("sudo containerlab destroy -t csrceos01.clab.yml --cleanup", shell=True)

#Borra la network entre telegraf y el router CSR1000v
def destruir_net():
	call("sudo chmod 666 /var/run/docker.sock", shell=True)
	call("docker network rm networkCSR1000v", shell=True)

#Funciones de ayuda
def mostrar_ayuda():
	ayuda_imagen_arista_nokia()
	print("")
	ayuda_lab_ca()
	print("")
	ayuda_lab_na()
	print("")
	ayuda_prepare()
	print("")
	ayuda_network_1000v()
	print("")
	ayuda_destruir_lab()
	print("")
	ayuda_destruir_net()
	print("")
	print("help <cmd>             ---> para mostrar esta pantalla de ayuda o solo la ayuda de un comando.")
	print("\tParámetros:")
	print("\t\t<cmd> -> opcional: para mostrar la ayuda de un único comando.")

def ayuda_imagen_arista_nokia():
	print("imagenes                 ---> para instalar las imagenes de los routers del laboratorio. En concreto serán un router Nokia y el router Arista 4.26.4M.")

def ayuda_lab_ca():
	print("labca                    ---> para crear el laboratorio de containerlab con un router Arista y uno de Cisco.")

def ayuda_lab_na():
	print("labna                    ---> para crear el laboratorio de containerlab con un router Arista y uno de Nokia.")

def ayuda_prepare():
	print("prepare                  ---> para habilitar la configuración inicial con netconf en el router Arista.")

def ayuda_network_1000v():
	print("net1000v                 ---> para crear la network entre telegraf y el router CSR1000v despues de haber desplegado ambos contenedores.")

def ayuda_destruir_lab():
	print("deslab                   ---> para borrar el laboratorio.")

def ayuda_destruir_net():
	print("desnet                   ---> para borrar la network entre telegraf y el router CSR1000v.")

#Inicio del script

#Comprobamos que nos pasan más de dos argumentos
if len(sys.argv) < 2:
	print("Comandos disponibles:")
	print("")
	mostrar_ayuda()
	sys.exit()

#Ordenes
if sys.argv[1] == "imagenes":
	instalar_imagen_arista_nokia()
elif sys.argv[1] == "labca":
	crear_lab_ca()
elif sys.argv[1] == "labna":
	crear_lab_na()
elif sys.argv[1] == "prepare":
	preparar_entorno()
elif sys.argv[1] == "net1000v":
	crear_network_1000v()
elif sys.argv[1] == "deslab":
	destruir_lab()
elif sys.argv[1] == "desnet":
	destruir_net()
elif sys.argv[1] == "help":
	if len(sys.argv) > 2:
		if (sys.argv[2] == "imagenes"):
			ayuda_imagen_arista_nokia()
		elif (sys.argv[2] == "labca"):
			ayuda_lab_ca()
		elif (sys.argv[2] == "labna"):
			ayuda_lab_na()
		elif (sys.argv[2] == "prepare"):
			ayuda_prepare()
		elif (sys.argv[2] == "net1000v"):
			ayuda_network_1000v()
		elif (sys.argv[2] == "deslab"):
			ayuda_destruir_lab()
		elif (sys.argv[2] == "desnet"):
			ayuda_destruir_net()
		else:
			mostrar_ayuda()
	else:
		mostrar_ayuda()

#Consola con datos
else:
	print("Orden no disponible.")
	print("Inténtelo de nuevo con alguno de estos comandos:")
	mostrar_ayuda()
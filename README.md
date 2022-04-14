# TFG_NETCONF
Trabajo de fin de grado realizado por Andrés Ripoll, el cual contiene scripts tanto para la instalación de los laboratorios virtualizados, como de los de prueba del escenario.

## Instalación
Para la correcta instalación del escenario, ejectutar el archivo instalacion.py en la carpeta pesonal. Todos los comandos vienen explicados en el script, y son los siguientes:

* Instalación de containerlab:
```bash
python3 instalacion.py containerlab
```

* Instalación de docker:
```bash
python3 instalacion.py docker
```

## Configuración
Una vez instalado todo lo necesario para arrancar el escenario, arrastrar el archivo configuracion.py, que se encuentra en la carpeta Instalacion, hasta la carpeta clab-quickstart que se ha creado previamente al instalar containerLab. Todos los comandos vienen explicados en el script, y son los siguientes:

* Instalación y configuración de las imágenes de los routers(se necesita un ordenador con al menos dos núcleos):
```bash
python3 configuracion.py imagenes
```

* Puesta en marcha del laboratorio de containerLab:
```bash
python3 configuracion.py laboratorio
```

* Habilitar la configuración inicial con netconf en el router Arita:
```bash
python3 configuracion.py prepare
```
*Nota: Se recomienda usar estos tres comandos en el orden en el que están expuestos aquí.*

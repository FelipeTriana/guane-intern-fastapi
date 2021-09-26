# Ejecutando el docker-compose

Desplegara toda la infraestructura con los contenedores que corresponden al worker de celery, flower, redis, la aplicacion y la base de datos mysql: 

```console
docker-compose up
``` 

Una vez desplegada la infraestructura podra acceder a la documentacion de la aplicacion en el localhost:8001/docs y a flower en el localhost:5556


# Ejecutando sin docker-compose

Nota: Si se ejecuta sin docker-compose se deberia tener la infraestructura localmente.

## Crear el entorno virtual:

Primero se debe crear un entorno virtual, en este caso fue creado con conda y con una version de python 3.9.7

```console
conda create --name guane-fastapi python=3.9
```


## Activar el entorno virtual con conda:

```console
conda activate guane-fastapi
```


## Instalar dependencias

```console
pip install -r requeriments.txt
```


## Correr el proyecto con uvicorn

Correr la funcion app en el modulo main

```console
uvicorn main:app --reload
```

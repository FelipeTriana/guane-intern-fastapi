# Ejecutando el proyecto por primera vez

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

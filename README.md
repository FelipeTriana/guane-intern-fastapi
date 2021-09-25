# Ejecutando el proyecto por primera vez

Primero se debe crear un entorno virtual, en este caso fue creado con conda y con una version de python 3.9


## Activar el entorno virtual con conda:

```console
conda activate guane-fastapi
```


## Instalar dependencias

```console
pip install -r requeriments.txt
```


## Correr el proyecto con uvicorn

This means, run app function in app module

```console
uvicorn main:app --reload
```

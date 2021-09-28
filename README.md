# guane-intern-fastapi

App para aplicar al perfil de desarrollador backend en Guane Enterprises. 

Se esta utilizando el framework de python FastAPI, MySQL como base de datos, Celery como cola de tareas, Redis como message broker y Flower para monitorear las tareas de Celery.


# Ejecutando el docker-compose

El siguiente comando desplegara toda la infraestructura que corresponde al worker de celery, flower, redis, la base de datos de mysql y la aplicacion: 

```console
docker-compose up --build
``` 

Nota: Solo la primera vez que se lanza el comando el contenedor de MySQL suele desplegarse despues que el de la app, en caso de presentar problemas de conexion con mysql cancelar el proceso con "ctrl + c" y volver a lanzar el comando:

```console
docker-compose up 
``` 

Una vez desplegada la infraestructura podra acceder a la documentacion de la aplicacion en el http://localhost:8001/docs y a flower en el http://localhost:5556 donde podra monitorear la llamada a una tarea simple de celery cuando se hace un llamado al endpoint POST: ​/api​/dogs​/celery​/{user_id}​/ 


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

```console
uvicorn app.main:app --reload
```

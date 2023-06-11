# Trabajo Integrador - Sistemas Distribuidos

## Descripción
La aplicación desarrollada simula un comportamiento de un pool de preguntas que en función del tiempo y las preguntas correctas, devuelve la posición alcanzada hasta ese momento al finalizar el juego.
Contiene un cliente, un servidor (ambos escritos en Python) y una base de datos key-value Redis.
Estos componentes se encuentran dockerizados.

Las docker images utilizadas se encuentran en hub.docker.com:
- https://hub.docker.com/r/emilianof/kajut-client
- https://hub.docker.com/r/emilianof/kajut-server

## Manifests
En los manifiestos de kubernetes se crean los siguientes objetos de kubernetes:
- 0-redis.yaml : contiene declarado el pod llamado redis en el que corre la imagen de redis sobre un Alpine Linux y el objeto service llamado redis-cluster.
- 1-client.yaml : contiene objetos service con un Load Balancer y deployment con el container donde corre el cliente.
- 2-server.yaml : contiene un objeto deployment con un contenedor donde corre el servidor.

## Ejecución
Para hacer un deploy de los objetos sobre el cluster, ejecutar:

    kubeclt apply -f ./0-redis.yaml
    kubeclt apply -f ./1-client.yaml
    kubeclt apply -f ./2-server.yaml

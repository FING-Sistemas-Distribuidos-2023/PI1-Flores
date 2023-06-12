# Trabajo Integrador - Sistemas Distribuidos

## Descripción
La aplicación desarrollada simula un comportamiento de un poll de preguntas que en función del tiempo y las preguntas correctas, devuelve la posición alcanzada hasta ese momento al finalizar el juego.
Contiene un cliente, un servidor (ambos escritos en Python) y una base de datos key-value Redis.
Estos componentes se encuentran dockerizados.

Las docker images utilizadas se encuentran en hub.docker.com:
- https://hub.docker.com/r/emilianof/kajut-client
- https://hub.docker.com/r/emilianof/kajut-server

## Manifests
En los manifiestos de kubernetes se crean los siguientes objetos de kubernetes:
- 0-redis-sts.yaml 1-redis-svc.yaml: contiene declarado el pod llamado redis en el que corre la imagen de redis sobre un Alpine Linux y el objeto service llamado redis-cluster.
- 2-server.yaml : contiene un objeto deployment con un contenedor donde corre el servidor.
- 3-client.yaml : contiene objetos service con un Load Balancer y deployment con el container donde corre el cliente.

## Ejecución
Para hacer un deploy de los objetos sobre el cluster, ejecutar:

```sh
kubectl apply -f 0-redis-sts.yaml
kubectl apply -f 1-redis-svc.yaml
kubectl exec -it redis-cluster-0 -- redis-cli --cluster create --cluster-replicas 1 $(kubectl get pods -l app=redis-cluster -o jsonpath='{range.items[*]}{.status.podIP}:6379 '| sed 's/.\{6\}$//')
kubectl apply -f 2-server.yaml
kubectl apply -f 3-client.yaml
```

O aplicar el script `deploy.sh`

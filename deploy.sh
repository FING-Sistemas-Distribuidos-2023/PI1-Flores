#!/bin/bash

kubectl apply -f 0-redis-sts.yaml
kubectl apply -f 1-redis-svc.yaml
kubectl exec -it redis-cluster-0 -- redis-cli --cluster create --cluster-replicas 1 $(kubectl get pods -l app=redis-cluster -o jsonpath='{range.items[*]}{.status.podIP}:6379 '| sed 's/.\{6\}$//')
kubectl apply -f 2-server.yaml
kubectl apply -f 3-client.yaml

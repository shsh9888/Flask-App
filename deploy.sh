#!/bin/sh

kubectl create deployment restserver --image=gcr.io/lab7-258103//flaskapp:latest
kubectl expose deployment restserver  --type=LoadBalancer --port 5000 --target-port 5000
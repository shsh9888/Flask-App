#!/bin/sh

kubectl create deployment flaskapp --image=gcr.io/lab7-258103/flaskapp:3.0
kubectl expose deployment flaskapp  --type=LoadBalancer --port 5000 --target-port 5000
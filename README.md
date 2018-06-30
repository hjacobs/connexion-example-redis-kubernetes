# Connexion Example REST Service with Redis Store

This example application implements a very basic "pet shop" REST service using the [Connexion](https://github.com/zalando/connexion) Python library.

## Local Development

```
pipenv install --dev
pipenv shell
docker run -d --name connexion-example-redis -p 6379:6379 redis:4-alpine
./app.py
xdg-open http://localhost:8080/ui/
```

## Deploying to Kubernetes (Minikube)

Start Minikube:

```
minikube start
```

Build the Docker image:

```
eval $(minikube docker-env)
docker build -t connexion-example:local-minikube .
```

Deploy to Kubernetes:

```
kubectl apply -f deploy/
```

Wait for pods to come up:

```
kubectl get pod
```

Create a pet:

```
url=$(minikube service connexion-example --url)
curl -X PUT $url/pets/susie -d '{"animal_type": "cat", "name": "Susie", "tags": {"color": "black"}}' -H Content-Type:application/json
```

Get all pets:

```
curl $url/pets
```

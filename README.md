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

Start [Minikube](https://github.com/kubernetes/minikube):

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

Simple load test with [Vegeta](https://github.com/tsenart/vegeta):

```
echo "GET $url/pets" | vegeta attack -rate 100 -duration 60s | vegeta report
```

The output should look something like this (depends on your hardware/VM configuration):

```
Requests      [total, rate]            6000, 100.02
Duration      [total, attack, wait]    1m0.034341468s, 59.98999991s, 44.341558ms
Latencies     [mean, 50, 95, 99, max]  41.344672ms, 46.279545ms, 52.171431ms, 54.320335ms, 72.515124ms
Bytes In      [total, mean]            3156000, 526.00
Bytes Out     [total, mean]            0, 0.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:6000
Error Set:
```

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

## Docker

```
docker build -t connexion-example .
docker run -it -p 8080:8080 connexion-example
```

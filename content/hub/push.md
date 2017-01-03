---
next: /hub/tags
prev: /hub/register
title: Publikowanie
weight: 32
---

### Personalizacja obrazu

Wprowadźmy coś od nas do naszej aplikacji:

```
@app.route("/")
def hello():
    return "<h1>Hello, I'm Imię i naziwsko!</h1>"
```

zbudujmy obraz ale z nową nazwą:
```
$ docker build -t $HUB_ID/hello-flask .
```

{{% notice note %}}
Docker Hub grupuje obrazy w **repozytoria**, których nazwa staje się częścią obrazu,
np. `mesoscloud/mesos-master` to obraz **mesos-master** w repozytorium **mesoscloud**.
Tylko oficjalne obrazy mogą być publikowane bez repozytorium w nazwie, np. **jenkins**.
{{% /notice %}}

### Opublikowanie na Docker Hub

Zbudowany lokalnie obraz możemy opublikować poleceniem:
```
$ docker push $HUB_ID/hello-flask
```

Obraz powinien się pojawić na naszej stronie domowej [Docker Hub](https://hub.docker.com/).

### Uruchomienie opublikowanego obrazu

Zapytaj sąsiada o jego **Docker Hub** i spróbuj uruchomić jego obraz:

```
$ docker run -it -p 8080:5000 <id_sąsiada>/hello-flask
```

Jego aplikacja powinna być dostępna pod adresem {{< host-url type="docker" port="8080" >}}

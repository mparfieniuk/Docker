# Publikowanie obrazów

### Docker Registry, Docker Hub

### [Docker Hub](https://hub.docker.com/)

Rejestrujemy się używając formularza *New to Docker?*:

![Signup](/img/hub_signup.png)

Po utworzeniu konta na *Docker Hub* możemy skojarzyć je z naszym klientem przez wykonanie:

```
$ docker login
```

Dla ułatwienia dalszych instrukcji zapisujemy **Docker Hub ID** pod jakim się
zarejestrowaliśmy w zmiennej środowiskowej:

```
$ export HUB_ID="<wstaw swoje ID>"
```

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

### Stabilna wersja

Każdy obraz może mieć wiele wersji, którą są oznaczane **tagami**. Stabilna werjsa
powinna być zawsze oznaczona tagiem **latest** i taka wersja jest używana domyślnie
we wszystkich komendarch **docker**. Tagi obbrazów widoczne są na ich liście:

```
$ docker images
```

### Tagi wersji

Wiele obrazów oznacza kolejne wydania wersjami w postaci numerycznej, np. **1.0**, **3**.
Oznaczmy nasz obraz wersją **1.0** jako pierwsze jego wydanie:

```
$ docker tag $HUB_ID/hello-flask $HUB_ID/hello-flask:1.0
```

Nowo utworzona wersja powinna zostać opublikowana:

```
$ docker push $HUB_ID/hello-flask:1.0
```

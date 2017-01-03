# Docker Compose

### Łatwy development w kilku kontenerach

### Kilka kontenerów jako całość

Zamiast uruchamiać kolejne komendy **docker run** i łączyć ręcznie kontenery
możemy użyć narzędzia **Docker Compose**. Dzięki niemu możemy deklaratywnie w jednym
pliku zdefiniować środowisko składające się z kilku działających kontenerów.
W tym celu tworzymy plik **docker-compose.yml**:

```
version: "2"
services:
  mongo:
    image: mongo
  express:
    image: mongo-express
    ports:
      - "8081:8081"
```

Możemy teraz uruchomić połaczone kontenery jedną komendą:

```
$ docker-compose up -d
```

To jedno polecenie wystarczyło do wystartowania bazy danych i spiętej z nią aplikacji
pod adresem {{% host-url type="docker" port="8081" %}}.

### Prywatna sieć w ramach jednej aplikacji

Docker compose tworzy odatkową sieć, w której znajdują się i są między sobą widoczne
zdefiniowane kontenery.

```
$ docker network ls
```

Konteneery w ramach swojej sieci mogą się do siebie odwoływać przez swoje nazwy usług.
Możemy to sprawdzić zaglądając do kontenera aplikacji:

```
$ docker exec -it <id_kontenera_mongo_express> bash
```

Kontener **mongo** widoczny jest w środku przez swoją nazwę:

```
$ ping mongo
```

### Zatrzymanie grupy kontenerów

Uruchomiona grupa kontenerów może też być zatrzymana jako całość:
```
$ docker-compose stop
```

> Gotowy [docker-compose.yml](/compose/docker-compose.yml)

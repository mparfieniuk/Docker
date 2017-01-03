---
next: /communication/volumes
prev: /communication
title: Zmienne środowiskowe
weight: 41
---

### Przekazywanie informacji do kontenera

Obrazy mogą używać zmiennych śroodwiskowych podczas uruchmiania kontenera, np.
[hasło do ArangoDB](https://github.com/arangodb/arangodb-docker/blob/b29a6ffa3d8914781f24d7468d7ff368cabac623/jessie/2.8.9/docker-entrypoint.sh#L27).

Uruchamiając kontener możemy podać wartość zmiennej środowiskowej przez przełącznik **-e**:
```
$ docker run -e ARANGO_ROOT_PASSWORD=workshop -p 8089:8529 arangodb:2.8
```

Pod adresem {{< host-url type="docker" port="8089" >}} powinna być dostępna konsola
bazy danych ArangoDB, do której możemy się zalogować podając **root** jako uzytkownika
i **workshop** jako hasło.

---
next: /build/layers
prev: /build/hello-flask
title: Informacja o uruchomieniu
weight: 22
---

### Kontrakt pomiędzy programistą i administratorem

Możliwość podania dowolnej komendy w `docker run` pozwala na szybkie testowanie
aplikacji i samego obrazu podczas ich developmentu.

Docker daje nam więcej. Wprowadza pewnego rodzaju kontrakt między aplikacją a jej
środowiskiem uruchomieniowym. Administratow nie musi ręczenie definiować komendy,
którą należy podać żeby uruchomić aplikację w kontenerze, nie musi też przeglądać
kodu żeby dowiedzieć się jakie na jakich portach ta aplikacja coś udostępnia.

#### Jak uruchomić twoją aplikację?

Każdy obraz może zdefiniować domyślną komendę, która zostanie uruchomiona w ramach
kontenerów na nim bazujących. Dla nasze aplikacji możemy zdefiniować wykonanie
`python hello.py` przez dyrektywę **CMD** w **Dockerfile**:

```
CMD ["python", "hello.py"]
```

#### Na jakich portach widoczna jest aplikacja?

Porty zajmowane przez aplikację to także część kontraktu zapisanego w **Dockerfile**.
Możemy jawnie powiedzieć podczas budowania obrazu, że nasza aplikacja staruje na
porcie **5000**:

```
EXPOSE 5000
```

Teraz możemy przebudować obraz

```
$ docker build -t hello-flask .
```

wystartować konterem w tle z domyślnym mapowaniem portów:

```
$ docker run -d -P hello-flask
```

i zobaczyć na jaki losowy port został przemapowany (kolumna **PORTS**):

```
$ docker ps
```

Każdy z kontenerów wystawia osobną instancję naszej aplikacji co można sprawdzić
przez wykonanie:

```
$ curl {{% host-url type="docker" port="32768" format="raw" %}}
```

podstawiając kolejne porty kontenererów wskazywane przez `docker ps`.

Na koniec ćwiczenia możemy zatrzymać wszystkie kontenery komendą:

```
$ docker stop $(docker ps -q)
```

> Gotowy [Dockerfile](/expose/Dockerfile)

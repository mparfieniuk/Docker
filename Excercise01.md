---
prev: /build
next: /build/expose
title: Prosta aplikacja webowa
toc: true
weight: 21
---

### Aplikcja webowa używająca [Flask](http://flask.pocoo.org/)

Flask to jeden z popularniejszych microframwerków, który bez zbędnych rzeczy
pozwala na zbudowanie aplikacji webowej.

<a id="easy-setup"></a>
#### Easy to Setup 

```
$ pip install Flask
$ python hello.py
 * Running on http://localhost:5000/
```

Kto ma *pythona*? Wersję *2* czy *3*? Kto ma *pip*? I wie jak go używać?
Dlatego spakujemy wiedzę, którą ma developer w jeden **przenośny i łatwo uruchamialny
obraz.**

### Zbudowanie obrazu docker

#### Katalog roboczy projektu

Tworzymy projekt **hello-flask**:

```
$ mkdir hello-flask
```

i przechodzimy do niego

```
$ cd hello-flask
```

tu powstanie nasz **Dockerfile** w którym zawrzemy całą wiedzę o naszej aplikacji.

#### Dockerfile

```
$ mcedit Dockerfile
```

{{% notice tip %}}
Na maszynie wirtualnej dostępne są 3 podstawowe edytory: **mcedit**, **micro**, **vim**.
{{% /notice %}}

##### Wybierz obraz bazowy

Każdy *Dockerfile* zaczynamy od okreśelnia obrazu bazowego przez podanie jego nazwy
w dyrektywie **FROM**. Dla naszej aplikacji będzie to obraz **ubuntu**:
```
FROM ubuntu
```

##### Podpisz się jako autor obrazu

Obrazy mogą być tworzone przez wiele osób i tak jak kod źródłowy będą łatwiejsze
w użyciu u utrzymaniu jeżeli każdy będzie mógł się skontaktować z autorem. Służy do
tego instrukcja **MAINTAINER**:
```
MAINTAINER Kamil Chmielewski <kamil.chm@gmail.com>
```

##### Potrzebujemy dodatkowych pakietów

Nasz obraz z **Ubuntu** potrzebuje odpowiednich pakietów. Dla aplikacji
Flask [będzie potrzebny](#easy-setup) **Python**, **pip** i sam **Flask**.

{{% notice note %}}
Docker sam w sobie nie wprowadza żadnego nowego mechanizmu do zarządzania pakietami.
Jeżeli chcemy coś zaintsalować to msuimy użyć menadżera pakietów wspieranego
przez system wybrany jako obraz bazowy. W przypadku Ubuntu będzie to **APT**.
{{% /notice %}}

##### Powiedz dockerowi jakimi poleceniami zbudować obraz 

Docker pozwala na kompozycję obrazu przez podanie listy następujących po sobie kroków,
które zostaną wykonane. Kolejne kroki do wykonania definiujemy używając instrukcji
**RUN**.

Instalacja pakietów w obrazie z **Ubuntu** to wykonanie poleceń **APT**:
```
RUN apt-get update
RUN apt-get install -y python-pip
```

Teraz możemy zainstalować samego Flaska:
```
RUN pip install Flask
```

##### Dodaj do obrazu swoją aplikację

Aplikacje webowa *hello world* to dzięki Flask jeden porsty plik **hello.py**,
który tworzymy w tym samym katalogu co nasz **Dockerfile**.

```python
# hello.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Docker!"

app.run("0.0.0.0")
```

Teraz możemy dodać naszą aplikację do obrazu przez dołączenie pliku **hello.py**.
Służy do tego komenda **COPY**, którą dodajemy do **Dockerfile**:

```
COPY hello.py /hello.py
moj szef jewst...
```

##### Zbuduj obraz

Mamy już wszystkie wymagane pakiety i samą aplikację w definicji naszego obrazu.
Możemy go teraz **zbudować** pod nazwą **hello-flask**:

```
$ docker build -t hello-flask .
```

##### Uruchom kontener

Uruchomienie aplikacji Flask to proste wykonanie naszego pliku za pomocą Pythona.
Możemy to teraz zrobić startując kontener w ramach zbudowanego obrazu:

```
$ docker run -it -p 8080:5000 hello-flask python hello.py
```

Po wykonaniu tej operacji na {{% host-url type="docker" port="8080" %}} widoczna
jest nasza nowa aplikacja.

> Efekty ćwiczenia: [Dockerfile](/hello-flask/Dockerfile), [hello.py](/hello-flask/hello.py)

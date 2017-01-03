# Budowanie obrazów

### Dockerfile i docker build


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
MAINTAINER Piotr Szwed <pszwed@gmail.com>
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

### Każdy obraz składa się z warstw

Docker buduje obrazy i kontenery nakładając na siebie kolejne warstwy systemu plików.
Każda warstwa woorzona jest raz i nie może być póniej zmieniana. Zmiany w systemie
plików są implementowane przez mechanizm *Copy-on-write*. Pozwala to uzyskać
współdzielenie wspólnych części obrazów i kontenerów, a tym samym oszczędzać zajmowane
przez nie miejsce.

#### Każdy krok budowania jest warstwą

Nasz obraz **hello-flask** to 12 warstw:

```
$ docker history hello-flask
```

#### Opytmalizacja zajętości dysku

```
$ docker images
```

#### Optymalizacja czasu budowania

W ramach jednego **Dockerfile** budowane są tylko te kroki, które zostały zmienione
albo kroki, które po nich następują.

Możemy zmienić tylko źródła naszej aplikacji czyli **hello.py**, np:

```
@app.route("/")
def hello():
    return "<h1>Hello from Docker!</h1>"
```

i zbudować obraz:

```
$ docker build -t hello-flask .
```

Wszystkie kroki przed skopiowaniem źródeł aplikacji znajdują się już w cache i są pomijane.
Wykonywane są tylko instrukcje zaczynające się od kroku skopiowania pliku **hello.py**.

[< Previous](/Introduction.md)  [Next>](/Publikowanie_obrazow.md)

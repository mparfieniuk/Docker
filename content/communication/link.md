---
prev: /communication/volumes
next: /gc
title: Łączenie kontenerów
weight: 43
---

### Mikrousługi lubią swoje kontenery

Dobra architektura oddziela od siebie niezależne technicznie komponenty. Stąd coraz
częściej słyszymy o mikrousługach. W takim podejściu apikacja korzystająca z bazy
danych powinna być od niej odpowiednio odseparowana. Jedynym połaczeniem powinien
być ściśle okreslony interfejs bazy danych i jej sterownika, udostępniony najczęściej
na jakimś porcie.

#### Baza danych

Jako bazę danych do ćwiczenia wykorzystamy **MongoDB** w najprostszej konfiguracji.
Ważna natomiast jest nazwa tworzonego kontenera:

```
$ docker run --name some-mongo -d mongo
```

Tym razem nie wystawiamy żadnych portów z kontenera:

```
$ docker ps
```

Kolumna **PORTS** pokazuje **27017/tcp** nie zmapowane w żaden sposób. Jak więc skorzystać
z takiej bazy danych jak nie możemy się do niej podłączyć?

#### Połączenia pomiędzy kontenerami

Docker udostępnia specjalny mechanizm pozwalający na *prywatne* połączenia w ramach
wielu kontenerów. Połaczenia mogą być zestawiane przy użyciu przełącznika **--link**:

```
$ docker run --link some-mongo:mongo -p 8081:8081 mongo-express
```

Komenda powyżej uruchamia osobny kontener z graficznym interfejsem bazy danych, który
jest połączny z bazą danych uruchomioną w kontenerze **some-mongo**. Sam interfejs
można zobaczyć pod adresem {{% host-url type="docker" port="8081" %}}.

#### Jak to się stało?

Mechanizm łączenia kontenerów bazuje na udostępnianiu informacji o kontenerach przez
zmienne środowiskowe. Możemy sprawdzić to w nowym kontenerze połączonym do kontenera
z bazą danych:

```
$ docker run -it --link some-mongo:mongo hello-flask bash
```

możemy teraz obejrzeć wszytkie zmienne środowiskowe wykonując:

```
$ export
```

linkując kontener **some-mongo** pod nazwą **mongo** otrzymaliśmy szereg zmiennych
z prefixem **MONGO_** pozwalających nam na wykonanie połączenia. Nasza aplikacja
może teraz skorzystać ze zmiennej **MONGO_PORT_27017_TCP** żeby połączyć się
do dowolnego połaczonego kontenera, w którym została uruchomiona baza *MongoDB*.

Technicznie stworzony został nowy wirtualny interfejs wykorzystywany do komunikacji
pomiędzy kontenerami. Możemy go zobaczyć (**veth**) wykonując:

```
$ ifconfig
```

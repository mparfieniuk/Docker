# Komunikacja z kontenerem

### Zmienne środowiskowe, dysk, sieć


### Dane w kontenerze są efemeryczne

Wszystkie operacje wykonywane w ramach kontenera na systemie plików są widzoczne tylko
dla niego i nie mogą zostać ponownie użyte przez inne kontenery.

Uruchom jeszcze raz bazę ArangoDB jeżeli zamknąłeś ją w poprzenim ćwiczeniu:
```
$ docker run -e ARANGO_ROOT_PASSWORD=workshop -p 8089:8529 arangodb:2.8
```

Zaloguj się do niej po adresem {{< host-url type="docker" port="8089" >}}

#### Modyfikacja danych w kontenerze

Wybierz przycisk **Add collection** w za kładce **Collections**:
![Add collection](/img/arango_add_collection.png)

i podaj dowolną nazwę kolekcji w nowym okienku zatwierdzając jej dodanie.

Zatrzymaj kontener w maszynie wirtualnej przez **CTRL+C**, po czym uruchom taki sam
kontener ponownie:
```
$ docker run -e ARANGO_ROOT_PASSWORD=workshop -p 8089:8529 arangodb:2.8
```

Jeżeli przejdziesz jeszcze raz do zakładki **Collections** w konsoli *ArangoDB*
zobaczysz, że dodana przez Ciebie kolekcja znikła.

#### Zapisywanie stanu poza kontenerem

Jeżeli chcemy użyć wielokrotnie jakiś danych w wielu kontenerach powinniśmy użyć
woluminów danych. Wolumin musi być najpierw zadeklarowany
w [Dockerfile](https://github.com/arangodb/arangodb-docker/blob/b29a6ffa3d8914781f24d7468d7ff368cabac623/jessie/2.8.9/Dockerfile#L41):

```
VOLUME ["/var/lib/arangodb", "/var/lib/arangodb-apps"]
```

ArangoDB definiuje 2 ścieżki w kontenerze, które będą przechowywane poza kontenerem.
Na potrzeby ćwiczenia zdefiniujemy tylko pierwszy z woluminów. W tym celu utworzymy
lokalny katalog na dane ArandoDB:
```
$ mkdir -p /tmp/arangodb
```
i nadamy do niego odpowiednie uprawnienia
```
$ sudo chown 999:999 /tmp/arangodb
```
Uruchamiając taki kontener możemy możemy zmapować nasz nowy katalog jako wolumin dzięki
przełącznikowi **--volume** lub **-v**:

```
$ docker run -e ARANGO_ROOT_PASSWORD=workshop -p 8089:8529 -v /tmp/arangodb:/var/lib/arangodb arangodb:2.8
```

Dodaj teraz ponownie kolekcję w konsoli *ArangoDB*. Zatrzymaj teraz kontener (**CTRL+C**)
i uruchomo ostatnie polecenie jeszcze raz uruchamiając kolejny kontener z persystentnym
woluminem. Kolekcja utworzona w jednym kontenerze powinna być teraz zapisywana pomiędzy
kolejnymi uruchomieniami.

Dane z kontenera będą też dostępne zamontowanym systemie plików
```
$ ls /tmp/arangodb/
```
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

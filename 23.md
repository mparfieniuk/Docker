---
next: /hub
prev: /build/expose
title: Warstwy
weight: 23
---

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

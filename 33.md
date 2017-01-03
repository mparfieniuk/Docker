---
next: /communication
prev: /hub/push
title: Wersjonowanie
weight: 33
---

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

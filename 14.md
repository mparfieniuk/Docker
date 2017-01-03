---
prev: /introduction/package_once
next: /build
title: Obrazy i kontenery
toc: true
weight: 14
---

### obraz => `docker run` => kontener

### Wiele kontenerów z jednego obrazu

```
$ docker ps -a
```

### Zainstalowane obrazy

```
$ docker images
```

#### Jak zainstalować obraz przed pierwszym uruchomieniem?

```
$ docker pull alpine
```

kolejne uruchomienia używają pobranego wczesniej obrazu

```
$ docker run alpine cat /etc/alpine-release
```

---
next: /gc/automatic
prev: /gc
title: Ręczne usuwanie śmieci
weight: 51
---

### Jakich śmieci?

Każde uruchomienie kontenera pozostawia po sobie jego stan. Wszystkie pozostałości
po starych kontenerach możemy zobaczyć dodając przełącznik `-a` do komendy `ps`:
```
$ docker ps -a
```

#### Usuwanie pojedynczego kontenera

Do usuwania starych kontenerów służy komenda:
```
$ docker rm <id_kontenera>
```

#### Usuwanie wszystkich nieaktywnych kontenerów

Możemy też połączyć komendy `rm` i `ps` żeby usunąc wszystkie nieaktywne kontenery:
```
$ docker rm $(docker ps -qa)
```

### A co z obrazami?

Wszystkie przechowywane na hoście obrazy i ich rozmiary możemy zobaczyć wykonując:
```
$ docker images
```

Jeżeli uznamy, że jakieś z nich nie będą nam już potrzebne to możemy je usunąć komendą:
```
$ docker rmi <id_obrazu>
```

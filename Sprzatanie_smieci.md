
# Sprzątanie śmieci

### Jak nie zapełnić dysku?

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

### Opcja --rm

Możemy powiedzieć dockerowi żeby autoamtycznie usunął kontener po jego zatrzymaniu
używając opcji `--rm`:
```
$ docker run --rm -it -p 8080:8080 jenkins
```

Po zakończeniu pracy takiego kotenera przez **CTRL-C** zostanie on automatycznie
usunięty:
```
$ docker ps -a
```

Nie działa to jednak w połączniu z przełącznikiem `-d` i ma wiele innych wad, stąd
przed wydaniem dockera [1.13](https://github.com/docker/docker/pull/20848) musimy
sobie z tym radzić inaczej.

### Projekt [docker-clean](https://github.com/zzrotdesign/docker-clean)

#### Instalacja

```
curl -s https://raw.githubusercontent.com/ZZROTDesign/docker-clean/v2.0.4/docker-clean |
sudo tee /usr/local/bin/docker-clean > /dev/null && \
sudo chmod +x /usr/local/bin/docker-clean
```

#### Bezpieczne usuwanie śmieci

Jeżeli chcemy usunąć wszystkie pozostałości po już nie używanych kontenerach wystarczy
jedno polecenie:
```
$ docker-clean images
```

#### Wyzerowanie dockera

Jeżeli chcemy zatrzymać wszystkie działające kontenery i przywrócić dockera do momentu
instalacji możemy użyć polecenia:
```
$ docker-clean all
```

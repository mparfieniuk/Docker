---
next: /introduction/package_once
prev: /introduction/jenkins
title: A może Docker?
toc: true
weight: 12
---

```bash
$ docker run -d -p 8080:8080 jenkins
```

#### teraz wejdź na

{{% host-url type="docker" port="8080" %}}

### Co się stało?

Pod spodem został uruchomiony kontener Docker z obrazu Jenkins, a jego port 8080 został zmapowany na port 8080 naszego hosta.

### Kontener?

tak, Docker pozwala nam w łatwy sposób uruchamiać i kontrolować kontenery

```bash
$ docker ps
```

### Jak go zatrzymać?

można po ID kontenera

```bash
$ docker stop b8e6d1ea7a72
```

### Można też trochę bardziej deskryptywnie

nadając kontenerowi nazwę

```bash
$ docker run -d --name jenkins-demo -p 8080:8080 jenkins
```

pod którą będzie teraz znany nasz kontener

```bash
$ docker stop jenkins-demo
```

## Mogę więcej? :)

Możesz, np.

```bash
$ docker run -d -p 8080:8080 tomcat
```

#### i mamy tomcata na

{{% host-url type="docker" port="8080" %}}

### Skąd biorą się te kontenery?

```bash
$ docker search library
```

lub

#### https://hub.docker.com/explore/

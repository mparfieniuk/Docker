
# Wprowadzenie

### Docker Demo

### Np. [Jenkinsa](https://jenkins.io/)?

![Jenkins logo](https://jenkins.io/images/226px-Jenkins_logo.svg.png)

1. Download Jenkins
1. http://mirrors.jenkins-ci.org/war-stable/latest/jenkins.war
1. Oracle JDK? Open JDK?
1. Tomcat? Jetty?
1. Jaki użytkownik? Katalog roboczy?
1. Jakie porty udostępnia?


#### Kto ma znać odpowiedzi na te pytania? Developer? Admin? DevOps? :P

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

#### Docker Hub

https://hub.docker.com/_/jenkins/

#### Dockerfile źródłem prawdy

![Dockerfile links](/img/hub_dockerfile_links.png)

https://github.com/jenkinsci/docker/blob/master/Dockerfile

#### Jak to wygląda w środku?

```
$ docker run -it jenkins /bin/bash
```

```
$ ls /usr/share/jenkins/
```
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

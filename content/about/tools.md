---
next: /introduction
prev: /about/instructor
title: Narzędzia
toc: true
weight: 3
---

### Połaczenie SSH

#### user: `student`

#### pass: `learning`

#### Możliwe z terminala

```bash
$ ssh student@{{% host-name type="docker" %}}
```

#### Możliwe z przeglądarki

{{% host-url type="docker" port="2222" %}}

### Zaloguj się

i wykonaj `docker -v`

```bash
student@{{% host-name type="docker" %}}:~$ docker -v
Docker version 1.12.1, build 23cf638
```

### Dostępne edytory

* mcedit
* micro
* vim

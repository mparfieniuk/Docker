FROM ubuntu
MAINTAINER Kamil Chmielewski <kamil.chm@gmail.com>

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install Flask

COPY hello.py /hello.py

CMD ["python", "/hello.py"]

EXPOSE 5000

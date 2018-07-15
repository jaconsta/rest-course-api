# Django REST course.

Hello / Hola.

This is the code reference of my REST book using Django. You can access it [here](http://rest-course.jaconsta.com/book/).

Este es el código que se desarrolla en el libro del curso REST usando Django el cual puedes [ver acá](http://rest-course.jaconsta.com/book/).

## Quick start

Install [docker](https://docker.com)

Build the image

```sh
$ docker build . -t generador_memes_api
```

Run it

```sh
$ docker run -d -p 8000:8000 generador_memes_api
```

Just in case:

Execute the shell

```sh
$ docker exec -it <container_id/name> sh
```

Start / stop the built container without creating a new one:

Start:

```sh
$ docker container start <container_id/name>
```

Stop:

```sh
$ docker container stop <container_id/name>
```

## Installation

You require Python 3.5 or greater.

Create your virtual environment. And install the dependencies.

```sh
(my_env)$ pip install -r requirements.txt
```

And run your server.

```sh
(my_env)$ python generador_memes/manage.py runserver
```

And enjoy.

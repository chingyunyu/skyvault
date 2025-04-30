# SkyVault

### Tech Stack

  - Django
  - SQLite
  - Nginx
  - Docker

### (Optional) Create and Activate Conda Environment

```sh
$ conda create -n skyvault python=3.11
$ conda activate skyvault
```

### Build Docker Image

```sh
$ docker-compose build
```

### (Optional) Initialize Database

```sh
$ docker-compose run web python manage.py makemigrations app
$ docker-compose run web python manage.py migrate
```

### Start Docker Containers

```sh
$ docker-compose up -d
```

### Access Web App

```sh
$ http://127.0.0.1
```

### (Optional) Run Pytest Tests

```sh
$ docker-compose run test
```

### Stop Docker Containers

```sh
$ docker-compose down
```
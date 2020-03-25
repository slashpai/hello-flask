# hello-flask

A simple web app using Flask

### Switch to your preferred python version and install flask library

```bash
pip install flask
```

### Set environment variable

From shell where which you will be running app, set envionment variable to test, verify you get this when execute `env` or `printenv`

```bash
export APP_COLOR=red
```

### Run app

```bash
python app.py
```

## Using Docker

### Build image

```bash
docker build -t hello-flask:v1 .
```

### Run Docker container

It runs in background mode, you can access from http://localhost:5000

```bash
docker run -d -p 5000:5000 --name hello-flask  hello-flask:v1
```

* To pass env variable `APP_COLOR` to docker container, New site is available here http://localhost:5001

    ```bash
    docker run -d -p 5001:5000 --name hello-flask-env --env APP_COLOR=blue  hello-flask:v1
    ```

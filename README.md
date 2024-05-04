# Start poetry project

## Create Project:

```bash
poetry new auth-server
```

## Change directory to project:

```bash
cd auth-server
```

## Add dependencies in pyproject.toml file and run the following command:

```bash
poetry install
```

## Add poetry virtualenv interpreter in VSCode

## Write main.py, settings.py, models.py

## Run tests:

```bash
poetry run pytest
```

## Run project in Poetry Environment:

```bash
poetry run uvicorn auth_server.main:app --host 127.0.0.1 --port 8000 --reload
```

## Open in Browser:

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

## Publish on the Web while running locally

### Install Ngrok:

[https://ngrok.com/docs/getting-started/](https://ngrok.com/docs/getting-started/)

### Run the following command to add your authtoken to the default ngrok.yml:

```bash
ngrok config add-authtoken 2bZGNZ3Mj3HdRxPt19defOl_7oFHsvr5AmM9A9UZUyhFn
```

### Deploy with your static domain:

```bash
ngrok http --domain=my-static-domain.ngrok-free.app 8000
```

### Open in Browser:

- [https://my-static-domain.ngrok-free.app/](https://my-static-domain.ngrok-free.app/)
- [https://my-static-domain.ngrok-free.app/docs](https://my-static-domain.ngrok-free.app/docs)
- [https://my-static-domain.ngrok-free.app/openapi.json](https://my-static-domain.ngrok-free.app/openapi.json)

### Now we will use this json to create GPT Action.

### Now create a Custom GPT here:

[https://chat.openai.com/gpts](https://chat.openai.com/gpts)

### Add the following server URL in the openapi.json file generated by FastAPI and paste it into action schema:

```json
"servers": [
    {
        "url": "https://my-static-domain.ngrok-free.app/"
    }
],
```

## Now Let's Containerize the App

[https://fastapi.tiangolo.com/deployment/docker/](https://fastapi.tiangolo.com/deployment/docker/)

### Create a Dockerfile.dev in the root directory

### Checking to see if Docker is running:

```bash
docker version
```

### Run hello_world for docker in cmd

```bash
docker run hello-world
```

### Building the Image for Dev:

```bash
docker build -f Dockerfile.dev -t dev-auth:v.0.1 .
```

### Check Images:

```bash
docker images
```

### Verify config

```bash
docker inspect dev-auth:v.0.1
```

### Running the Container for Dev:

```bash
docker run -d --name auth-cont1 -p 8000:8000 dev-auth:v.0.1
```

### Check container is running

```bash
docker ps
```

### Check all containers

```bash
docker ps -a
```

### Check container logs

```bash
docker logs <containerName>
```

### Check container logs in live mode

```bash
docker logs <containerName> -f    (-f mean follow live logs)
```

### Stop container

```bash
docker stop <containerName or id>
docker kill <containerId or name>
```

### Remove docker container

```bash
docker rm <containerName or id>
```

### Restart container

```bash
docker start <container Id or name>
```

### Test the Container

```bash
docker run -it --rm dev-auth:v.0.1 /bin/bash -c "poetry run pytest"
```

### Let's start dev container

- Install "dev containers" extension
- Start your Docker engine by Docker Desktop app
- Click on remote explorer

## Docker Compose

Docker Compose is a tool specifically designed to simplify the development and management of applications that consist of multiple Docker containers.

### Installing Docker Compose:

Docker Desktop includes Docker Engine, Docker CLI, and Docker Compose all in one package. Docker Desktop is available for Windows, macOS, and Linux.

Use the following command to check which version is installed:

```bash
docker compose version
```

### Docker Compose File

A Docker Compose file, written in YAML format, is the heart of defining and managing multi-container applications with Docker.

[More about Docker Compose File](https://docs.docker.com/compose/compose-file/compose-file-v3/)

### Running the application:

With this Compose file saved as compose.yml, you can use the following commands to manage your application:

```bash
docker compose up -d    # This builds the images (if needed) and starts the container in detached mode (background)
docker compose stop     # This stops the container
docker compose down     # This stops and removes the container
```

### Connection String (added to the .env file)

Here's the connection string you can use to connect to the PostgreSQL database from another container running in the same Docker network:

```bash
postgresql://ziakhan:my_password@PostgresCont:5432/mydatabase
```

### Install pgAdmin to connect to the Database

pgAdmin is the most popular and feature-rich Open Source administration and development platform for PostgreSQL.

[Download and Install pgAdmin 4](https://www.pgadmin.org/download/)

### Connect to our PostgreSQL Container:

- Host name/address: localhost
- Post: 5433 (note it is not the default 5432)
- Maintenance database: mydatabase
- Username: ziakhan
- Password: my_password

## Assignment

Create a separate database container for testing in the compose file. You don't need to use a volume for the test database since we don't care to persist test data between runs. Once you have created the test database and updated the .env file, run the tests.

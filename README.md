# Flask-GraphQL-API
Flask API using Graphene to query a MongoDB database. Containerized with Docker.

A simple learning project for Mongo and GraphQL (Graphene).


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Project Structure](#project-structure)
* [Features](#features)
* [Setup with Docker](#setup-with-docker)
* [Querying the API](#querying-the-API)
* [Improvements/To Do](#todo)


## General Information
In the past, I've primarily dealt with REST APIs and SQL databases. So, I felt it was time to dive into GraphQL and a NoSQL database. In this case, Graphene and MongoDB. This project started with the basic [graphene-mongo tutorial](https://codedthemes.com/demos/admin-templates/datta-able/react/docs/), and has grown to include more queries and create/update/delete mutations for each Mongo document. 

The testing is still in progress, as I've found testing GraphQL to be a tad tricky. As I learn, I'll continue to update the API, as I feel this is the best way to learn. 


## Technologies Used
- Flask, with the Flask-GraphQL extension
    - Flask-Mongoengine as the ORM
    - Graphene-mongo for GraphQL schema/querying
    - pytest, coverage, and mongomock for testing
    - gunicorn as the production WSGI server

- MongoDB, with prepopulated data
- Docker for containerization


## Project Structure
```
~/flask-graphql-api
    |-- docker-compose.yml
    |__ /backend
        |-- Dockerfile.api
        |-- run.py
        |-- populate_db.py
        |-- config.py
        |-- requirements.txt
        |-- .env
        |__ /api
            |__ /department
                |-- __init__.py
                |-- mutations.py
                |-- types.py
            |__ /employee
                |-- __init__.py
                |-- mutations.py
                |-- types.py
            |__ /role
                |-- __init__.py
                |-- mutations.py
                |-- types.py
            |-- __init__.py
            |-- models.py
            |-- routes.py
            |-- schema.py
        |__ /tests
            |-- __init__.py
            |-- test_api.py
    |__ /mongodb
        |-- Dockerfile.mongo
        |__ /data
            |-- ...
```

## Features
- GraphQL API querying a NoSQL dataset
    - Query all employees, departments, or roles
    - Query individual employees, departments, or roles
    - Mutate (create, update, delete) employees, departments, or roles


## Setup with Docker
Ensure you have docker installed.

```bash
docker --version
```

### Creating .env file
For this server to run, you must create a .env file within the package, setting the following parameters:
```bash
cd backend
touch .env
```

These are the .env variables, if your host/port/url etc vary, change it accordingly. Note that if you use Docker, your HOST will be the name of your service as defined in the docker-compose file, not localhost.
```bash
SECRET_KEY=
FLASK_APP=run.py

MONGODB_DB=<DB_NAME>
MONGODB_HOST=<DB_HOST>
MONGODB_PORT=<DB_PORT>
```
Set the secret key(s) to whatever you'd like (though they should be secure for production).


### Running the Server
Start the docker daemon and build the containers (sudo if Linux). You may not need to use sudo, or start the daemon, depending on your configuration.

```bash
sudo dockerd
sudo docker-compose up -d --build
```

To ensure everything is up and running, run docker ps
```bash
sudo docker ps
```

Start/stop containers using the following:

```bash
sudo docker container <start/stop> <container-name>
```

Or, stop and remove running containers with:
```bash
sudo docker-compose down
```

### Viewing the website
Site can be found here: http://127.0.0.1:5000 (for localhost)
GraphiQL interface at: http://127.0.0.1:5000/graphql


## Querying the API
Queries and mutations can be executed via the GraphiQL interface, or testing tools like Postman. To query all employees, returning all information including department, roles, manager, and tasks:
```
{
  allEmployees {
    edges {
      node {
        id,
        name,
        hiredOn,
        department {
          id,
          name
        },
        roles {
          edges {
            node {
              id,
              name
            }
          }
        },
        manager {
          id,
          name
        }
        tasks {
          edges {
            node {
              name,
              deadline
            }
          }
        }
      }
    }
  }
}
```


## TODO
TODO:
- Fix task mutations
- Update testing

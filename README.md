# Hitmen Challenge

Challenge for Jüsto Backend Developer


## Summary

API REST to create and list Hitmen and Hits.


## Features

- Hitmen:
    - Register a Hitman (if manager set isManager=true).
    - Get the Hitmen List.
    - Get the Hitman detail by ID.

- Hits:
    - Create a Hit.
    - Get the Hits List.
    - Get the Hit detail by ID.


## Pre-requirements

Download or clone this repo and put the [.env](https://drive.google.com/file/d/18FlJNZnKr6Y65kcStJbkOiio-1abt4Pl/view?usp=sharing) at the root of the project.

Is needed to get Make, Docker and Docker-Compose installed at local to run the project.

- Docker 
- Docker Compose
- Make


## Tech Stack

- Python
- Django
- Django Rest Framework
- PostgreSQL
- Docker
- Docker-compose


## Run with make

- Build
    ```sh
        $ make local-build
    ```
- Run
    ```sh
        $ make local-up
    ```

- Rebuild
    ```sh
        $ make local-rebuild
    ```

- Stop
    ```sh
        $ make local-stop
    ```

- Logs
    ```sh
        $ make local-backend-logs
    ```

- Run tests
    ```sh
        $ make local-test
    ```

## Run with Docker-Compose

- Build
    ```sh
        $ docker-compose -f docker-compose.yml build
    ```
- Run
    ```sh
        $ docker-compose -f docker-compose.yml up -d
    ```

- Rebuild
    ```sh
        $ docker-compose -f docker-compose.yml up -d --build
    ```

- Stop
    ```sh
        $ docker-compose -f docker-compose.yml stop
    ```

- Logs
    ```sh
        $ docker-compose -f docker-compose.yml logs -f backend
    ```


## Documentation

To see full project documentation Run the project and goto [API Swagger Docs](http://127.0.0.1:8080/api/v1/docs/)

- Login:
    - Login and get token. Please first create accounts, one as 'Boss' with the flag isBoss=true.

        ```
            POST /api/v1/login/
        ```

        ```
            {
                "email": "string",
                "password": "string"
            }
        ```

- Hitmen:
    - Register Hitman. Please first create accounts, one as 'Boss' with the flag isBoss=true.

        ```
            POST /api/v1/hitmen/register/
        ```

        ```
            {
                "name": "string",
                "email": "user@example.com",
                "password": "string",
                "desc": "string",
                "isActive": "Active",
                "isManager": false,
                "managedBy": null,
                "isBoss": true
            }
        ```

    - Get the list of the Hitmen.
    
        ```
            GET /api/v1/hitmen/
        ```

    - Get Hitman Detail.
    
        ```
            GET /api/v1/hitmen/{hitman_id}/
        ```

- Hits:

    - Create Hits:

        ```
            POST /api/v1/hits/create/
        ```

        ```
            {
                "assignee": 2,
                "desc": "string",
                "target": "string",
                "status": "ASSIGNED"
            }
        ```
    - Get the Hits.

        ```
            GET /api/v1/hits/
        ```
    
    - Get Hits details.

        ```
            GET /api/v1/hits/{hit_id}/
        ```

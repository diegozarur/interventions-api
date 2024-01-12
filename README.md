# Interventions API

This project is a simple API built with Flask and PostgreSQL. It provides basic CRUD operations for managing
interventions. Interventions have fields like wording, description, name, speaker, location, date of intervention, and
status.

## Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/) (version 2.7)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/project.git
    cd project
    ```

2. Copy the `.env.example` file to create a `.env` file:

    ```bash
    cp .env.example .env
    ```

3. Edit the `.env` file and provide values for the environment variables:

    ```bash
    nano .env
    ```

   Add your database credentials and other configuration details.

## Docker Setup

Build and start the Docker containers:

```bash
docker-compose up --build
```

To stop the Docker containers:

```bash
docker-compose down
```

## Database Initialization

1. Access the Flask container:

```bash
docker-compose exec web bash
```

2. Inside the container, run Flask-Migrate commands to initialize the database:

```bash
flask db init
flask db migrate
flask db upgrade
```

This will initialize the database and apply any initial migrations.

## Running the Application

With the containers running, the Flask application should be accessible at http://localhost:8000. You can access the API
and the frontend from this URL.


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

## Accessing the Interventions API

### List all Interventions

To retrieve a list of all interventions, you can make a `GET` request to the following endpoint:

```bash
curl -X GET http://localhost:8000/api/v1/interventions
```

### Get a Specific Intervention

To retrieve details of a specific intervention, replace <intervention_id> with the actual ID and make a GET request:

```bash
curl -X GET http://localhost:8000/api/v1/interventions/<intervention_id>
```

### Create a New Interventionn

To create a new intervention, make a POST request with the required data:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"wording":"New Intervention","description":"Description of the intervention","name":"John Doe","speaker":"Speaker Name","location":"Event Location","date_of_intervention":"2023-01-01 12:00:00"}' http://localhost:8000/api/v1/interventions
```

### Update an Intervention

To update an existing intervention, replace <intervention_id> with the actual ID and make a PUT request with the
updated data:

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"description":"Updated description"}' http://localhost:8000/api/v1/interventions/<intervention_id>
```

### Delete an Intervention

To delete an intervention, replace <intervention_id> with the actual ID and make a DELETE request:

```bash
curl -X DELETE http://localhost:8000/api/v1/interventions/<intervention_id>
```

## Flask-Restless

This project uses [Flask-Restless](https://flask-restless.readthedocs.io/) for creating a RESTful API with ease.
Flask-Restless simplifies the process of building RESTful APIs on top of Flask applications.

For more information about Flask-Restless, you can refer to
the [official documentation](https://flask-restless.readthedocs.io/).

### Quick Links

- [Flask-Restless Documentation](https://flask-restless.readthedocs.io/)

## Running the Application

With the containers running, the Flask application should be accessible at http://localhost:8000. You can access the API
and the frontend from this URL.


# Basic-CRUD-API-App
The CRUDApp API allows users to perform CRUD (Create, Read, Update, Delete) operations on data stored in the application.

# CRUD API with Flask(python) and MongoDB

## Setup Instructions
1. **Install Docker**: Follow the instructions for your operating system on the [Docker website](https://docs.docker.com/get-docker/).

2. **Clone the repository**:
    ```bash
    git clone https://github.com/VaibhavPatilVirus/Basic-CRUD-API-App.git
    cd Basic-CRUD-API-App
    ```

3. **Build and run the Docker containers**:
 - This will run Docker containers in dettached mode.
    ```bash
    docker-compose up --build -d
    ```
4. **Run API unit test**:
 - Command for running unit tests.
    ```bash
    python testing.py
    ```
5. **Verify all unit test ran successfully**:
  - The output should resemble the following.
    ```bash
    .......
    ----------------------------------------------------------------------
    Ran 7 tests in 0.131s

    OK
    ```

## API Endpoints
[For Detailed API documentation click here](API-Documentation.md)

- **POST /data**: Store JSON data
    - Example: `curl -u admin:secret -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://localhost:5000/data`

- **GET /data/{id}**: Retrieve JSON data by ID
    - Example: `curl -u admin:secret http://localhost:5000/data/{id}`

- **PUT /data/{id}**: Update JSON data by ID
    - Example: `curl -u admin:secret -X PUT -H "Content-Type: application/json" -d '{"key":"new_value"}' http://localhost:5000/data/{id}`

- **DELETE /data/{id}**: Delete JSON data by ID
    - Example: `curl -u admin:secret -X DELETE http://localhost:5000/data/{id}`

## Error Handling
- [For Detailed API documentation click here](API-Documentation.md)

## Testing
4. **Run API unit test**:
 - Output should looklike as below.
    ```bash
    python testing.py
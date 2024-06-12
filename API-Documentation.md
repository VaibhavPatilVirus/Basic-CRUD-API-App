# CRUDApp API Documentation

The CRUDApp API allows users to perform CRUD (Create, Read, Update, Delete) operations on data stored in the application.

## Base URL
The base URL for the API is: http://localhost:5000

## Endpoints

### 1. Create Data

- **URL:** `/data`
- **Method:** `POST`
- **Description:** Create a new data item.
- **Request Format:**
  - Content-Type: `application/json`
  - Body: JSON object containing data attributes.
    - `foo`: JSON attribute with some data.
    - `foo2`: Another JSON attribute with some data.
- **Response Format:**
  - Status Code: `201 Created`
  - Body: JSON object containing the ID of the created data item.
    ```json
    {
        "id": "<ObjectId>"
    }
    ```
- **Example:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name":"New Data","value":100}' http://localhost:5000/data
  ```

### 2. Get Data

- **URL:** `/data/<id>`
- **Method:** `GET`
- **Description:** Retrieve a specific data item by ID.
- **Request Format:** None
- **Response Format:**
  - Status Code: `200 OK`
  - Body: JSON object representing the data item.
- **Example:**
  ```bash
  curl http://localhost:5000/data/<id>
  ```

### 3. Update Data

- **URL:** `/data/<id>`
- **Method:** `PUT`
- **Description:** Update a specific data item by ID.
- **Request Format:**
  - Content-Type: `application/json`
  - Body: JSON object containing data attributes.
    - `foo`: JSON attribute with some data.
    - `foo2`: Another JSON attribute with some data.
- **Response Format:**
  - Status Code: `200 OK`
  - Body: JSON object containing a message indicating success.
    ```json
    {
        "message": "Data updated"
    }
    ```
- **Example:**
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"name":"Updated Data","value":200}' http://localhost:5000/data/<id>
  ```

### 4. Delete Data

- **URL:** `/data/<id>`
- **Method:** `DELETE`
- **Description:** Delete a specific data item by ID.
- **Request Format:** None
- **Response Format:**
  - Status Code: `200 OK`
  - Body: JSON object containing a message indicating success.
    ```json
    {
        "message": "Data deleted"
    }
    ```
- **Example:**
  ```bash
  curl -X DELETE http://localhost:5000/data/<id>
  ```

## Error Handling
- All error responses will have a JSON body containing an "error" key with an appropriate error message.
- Error responses will include appropriate HTTP status codes.

## Error Codes
- **400 Bad Request:** Invalid request format or data format.
- **404 Not Found:** Requested data item not found.
- **405 Method Not Allowed:** Invalid request method for the endpoint.
- **500 Internal Server Error:** Unexpected server error occurred.
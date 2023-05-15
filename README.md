## API - Generating Valid Cryptocurrency Addresses 

The project is a REST API that generates and stores encrypted cryptocurrency addresses and their corresponding private keys using Fernet key encryption. Currently, Bitcoin and Ethereum are the supported cryptocurrencies.

In order to recover from a disaster, the project uses a x_ref table linking encrypted private keys and addresses. This table ensures that the addresses can be recovered in the event of a catastrophe. Additionally, Fernet key encryption is used to ensure that the private keys remain secure.

While ideally the backup would be kept in a separate database, for development purposes the encryption and decryption key is generated every time the server is run. In a production environment, the key should be stored outside the code base and only accessible to the server hosting the application.

## Installation and Running with Docker

1. Clone the repository and navigate to the project directory. To start the API in a Docker container run at the root of the project:
    
    ```
    docker-compose up
    ```

2. You can run the tests by executing the following command at the root of the project:

    ```
    docker exec zeply-api python -m pytest -v tests
    ```

    This will execute the tests inside the running container at `tests/` directory.

## Installation and Running without Docker

The application works over an Ubuntu system and with Python 3.10.

1. Clone the repository locally.
2. Navigate to the api/ folder.
3. Install the requirements by running:
    ```
    pip install -r requirements.txt
    ```
4. Run the server by entering the command from the api/ folder:
    ```
    python -m app.main
    ```
5. This will make the server run locally, and the test message can be checked from the browser by hitting the URL http://localhost:8020.
6. To run the tests, also from the api/ directory, enter the command:
    ```
    python -m pytest -v tests
    ```

## API Usage

The API has four endpoints:

- `GET /`: Returns a test message.
- `GET /addresses`: Returns a list of all addresses stored in the database.
- `GET /addresses/{address_id}`: Returns a specific address with the given ID.
- `POST /addresses/generate`: Generates a new cryptocurrency address and stores it in the database. The request body should include the `currency` parameter, which is mandatory and should be set to either `btc` or `eth`.. All other parameters are optional.

Example payload:

```json
{
"currency": "btc",
"label": "My Bitcoin Address"
}
```

## Technologies Used

- Python 3.10
- FastAPI
- Docker
- SqliteDatabase

## Acknowledgements

This API was developed for an assessment test of Zeply. Developed by Kennedy Bacelar.

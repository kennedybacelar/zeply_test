## API - Generating Valid Cryptocurrency Addresses 

The project is a REST API that generates and stores encrypted cryptocurrency addresses and their corresponding private keys using Fernet key encryption. Currently, Bitcoin and Ethereum are the supported cryptocurrencies.

In order to recover from a disaster, the project uses a x_ref table linking encrypted private keys and addresses. This table ensures that the addresses can be recovered in the event of a catastrophe. Additionally, Fernet key encryption is used to ensure that the private keys remain secure.

While ideally the backup would be kept in a separate database, for development purposes the encryption and decryption key is generated every time the server is run. In a production environment, the key should be stored outside the code base and only accessible to the server hosting the application.

## Installation

Clone the repository and navigate to the project directory. Run `docker-compose up` to start the API.

## API Usage

The API has four endpoints:

- `GET /`: Returns a test message.
- `GET /addresses`: Returns a list of all addresses stored in the database.
- `GET /addresses/{address_id}`: Returns a specific address with the given ID.
- `POST /addresses/generate`: Generates a new cryptocurrency address and stores it in the database. The request body should include the `currency` parameter, which should be set to either `btc` or `eth`.

## Technologies Used

- Python 3.10
- FastAPI
- Docker
- SqliteDatabase

## Acknowledgements

The project was built by Kennedy Bacelar as an assessment test.

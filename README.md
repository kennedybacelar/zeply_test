## Project Name

The project is a REST API that generates cryptocurrency addresses and stores them in a database. It currently supports Bitcoin and Ethereum Crypto currencies and the corresponding private keys are encrypted before storage using a Fernet key.

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

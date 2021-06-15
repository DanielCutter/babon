# Babon

tinder for group projects

## Installation

Install [poetry](https://python-poetry.org/docs/).

Initialise using the lock file to install all dependencies.

```bash
poetry install
```

## Running Local Server

while inside the babon folder run:

```bash
poetry run python manage.py runserver
```
Server will be served on localhost:8000


## Migrating local DB

If there are reports of local database migrations missing apply using:

```bash
poetry run python manage.py migrate
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

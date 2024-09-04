# Fintual portfolio

This is a repository made to develop the fintual portfolio code challenge

## How to run the code

Assuming you have python installed in your machine and poetry as well, you can run the following command to install the dependencies:

```bash
poetry install
```

After that you can run the following command to start the server:

```bash
poetry run fastapi dev src/server.py
```

and access the openapi documentation in the following url:

```
http://localhost:8000/docs
```

## How to run the tests

To run the tests you can run the following command:

```bash
poetry run pytest
```

## How to verify code style is correct

To verify the code style is correct you can run the following command:

```bash
poetry run ruff check
```

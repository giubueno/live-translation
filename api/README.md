# Live Translation API

This is a FastAPI project designed to provide a robust and efficient web API for the Live Translation frontend.

## Prerequisites

- Python 3.7+
- pip
- Postgres
- Redis
- Kafka

## Quick Run

There is a script called **run** that will quickly initiate the API. Try it first, please.

```bash
./run
```

## Setup

### 1. Create a Virtual Environment

```bash
python3 -m venv env
```

### 2. Activate the Virtual Environment

```bash
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application
To run the FastAPI application, use the following command:
```bash
uvicorn main:app --reload
```
Replace main with the name of your Python file containing the FastAPI app instance.

## Accessing the API
Once the application is running, you can access the API documentation.
These endpoints provide interactive documentation for the API.

### Swagger UI
```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```
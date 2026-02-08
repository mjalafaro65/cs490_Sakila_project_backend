# Sakila Backend API

A lightweight Flask backend for working with the Sakila sample dataset (films, inventory, rentals, stores). This repository provides REST endpoints, schemas, and services to query film and rental data.

## Features
- REST API for Sakila film data
- Marshmallow schemas and SQLAlchemy models
- Service layer for business logic

## Requirements
- Python 3.11+ (project uses a virtualenv in `env/`)
- Dependencies listed in `requirements.txt`

## Quick Start
1. Clone the repo:

   git clone <repo-url>
   cd cs490_Sakila_project_backend

2. Create and activate a virtual environment (Windows):

   python -m venv env
   env\Scripts\Activate.ps1    # PowerShell
   env\Scripts\activate.bat    # CMD

3. Install dependencies:

   pip install -r requirements.txt

## Configuration
- See [config.py](config.py) for configuration options and environment variables.
- Typical env vars to set (examples):
  - `FLASK_APP=app.py`
  - `FLASK_ENV=development`
  - `DATABASE_URL` (your DB connection string used by `config.py`)

## Database
- This backend targets the Sakila sample database. Import the Sakila SQL dump into your database and update `DATABASE_URL` accordingly.
- There is no automatic seeder included; import sample data using the official Sakila SQL.

## Run (development)
1. Ensure virtualenv is active and env vars set.
2. Start the server:

   flask run

Or:

   python -m flask run

## API Overview
- Main resources live in the `resources/` folder (see [resources/film_resource.py](resources/film_resource.py)).
- Schemas are in [schemas/film_schema.py](schemas/film_schema.py).
- Business logic is in [services/film_service.py](services/film_service.py).

Example endpoints (confirm exact routes in `film_resource.py`):


- `GET /films/top?limit=10` — top films by some metric (branch suggests this endpoint)

## Project Structure
- `app.py` — application entry point
- `config.py` — configuration
- `extensions.py` — initialized Flask extensions
- `models/` — SQLAlchemy models (`film.py`, `inventory.py`, `rental.py`, `store.py`, `film_category`)
- `resources/` — Flask-RESTful resources
- `schemas/` — Marshmallow schemas
- `services/` — application business logic


## TODO / Improvements


## License
Add a `LICENSE` file with your chosen license (e.g., MIT).

---


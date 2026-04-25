# Stock Picker

Stock Picker is a FastAPI REST API for managing a personal stock watchlist with live price tracking via Yahoo Finance.

## Features

- Register, log in, and receive a JWT access token
- Password validation with length and special character requirements
- Add and remove stock tickers from a personal watchlist
- Fetch live prices for all watched tickers on demand
- Duplicate ticker and invalid ticker protection

## Tech Stack

- **FastAPI** — API framework
- **SQLAlchemy** — ORM
- **Alembic** — database migrations
- **SQLite** — database
- **yfinance** — live stock price data via Yahoo Finance
- **JWT (python-jose)** — authentication
- **passlib / bcrypt** — password hashing
- **pydantic-settings** — environment variable management

## Project Structure

```text
app/
├── core/
│   ├── dependencies.py   # DI composition root
│   └── security.py       # JWT and password utilities
├── db/
│   ├── base.py           # SQLAlchemy declarative base
│   └── session.py        # Database engine and session
├── models/               # SQLAlchemy ORM models
├── repositories/         # Database access layer
├── routers/              # API route handlers
├── schemas/              # Pydantic request/response schemas
└── services/             # Business logic layer
alembic/                  # Migration files
```

## Architecture

The project follows a layered architecture with dependency injection throughout:

```text
Router → Service → Repository → Database
```

- **Routers** — handle HTTP requests and responses, depend on services via FastAPI's `Depends()`
- **Services** — contain business logic, depend on repositories
- **Repositories** — handle all database access via SQLAlchemy
- **Schemas** — Pydantic models used for request validation and response serialization
- **Dependencies** — composition root wiring all layers together (`app/core/dependencies.py`)

## API Endpoints

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/auth/register` | No | Register a new user |
| POST | `/auth/login` | No | Login and receive JWT token |
| GET | `/watchlist/` | Yes | Get all watched tickers with live prices |
| POST | `/watchlist/` | Yes | Add a ticker to your watchlist |
| DELETE | `/watchlist/{ticker_symbol}` | Yes | Remove a ticker from your watchlist |

## Local Setup

### Prerequisites

- Python 3.11+
- Git

### 1. Clone the repository

```bash
git clone git@github.com:JasonComo/StockPicker.git
cd StockPicker
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the project root

```text
SECRET_KEY=your_secret_key_here
```

Do not put your secret key in source code.

### 5. Run migrations

```bash
alembic upgrade head
```

### 6. Start the server

```bash
python app/main.py
```

API will be running at `http://localhost:8000`

Swagger docs available at `http://localhost:8000/docs`

## Why I Built This

I built this tool to get hands-on experience with FastAPI. I'm interested in stocks/investing and wanted to build a project that integrated an external API, so this tool seemed like a good fit.
# Sovereign On-Premise Agentic AI Workbench — Backend

Backend service foundation for **SIH 2026 Problem Statement 26117**: Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work.

---

## 1. What the Backend Does

The backend acts as the core orchestration and business logic server for the workbench. It exposes RESTful APIs to interface with the frontend client, coordinates database transactions with PostgreSQL, and will manage agentic workflow orchestration, local model gateway dispatch, and audit logging for confidential industrial environments.

---

## 2. Tech Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.12+)
- **Server:** [Uvicorn](https://www.uvicorn.org/) (ASGI)
- **Database ORM:** [SQLAlchemy 2.x](https://www.sqlalchemy.org/)
- **Database Driver:** [psycopg 3](https://www.psycopg.org/psycopg3/)
- **Migrations:** [Alembic](https://alembic.sqlalchemy.org/)
- **Configuration & Validation:** [Pydantic v2](https://docs.pydantic.dev/) & [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- **Testing:** [pytest](https://docs.pytest.org/) & [HTTPX](https://www.python-httpx.org/)

---

## 3. How to Create the Python Environment

From inside the repository root or the `backend/` directory, create a Python virtual environment:

### Windows (PowerShell):
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Linux / macOS:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

---

## 4. How to Install Dependencies

Ensure your virtual environment is active, then run:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 5. How to Configure `.env`

Copy the example configuration file and adjust variables as required:

### Windows (PowerShell):
```powershell
Copy-Item .env.example .env
```

### Linux / macOS:
```bash
cp .env.example .env
```

### Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DATABASE_URL` | PostgreSQL connection URL with psycopg 3 driver | `postgresql+psycopg://postgres:password@localhost:5432/sih_2026` |
| `ENVIRONMENT` | Deployment environment (`development`, `staging`, `production`, `test`) | `development` |
| `DEBUG` | Enable debug logs and detailed error traces | `true` |

> [!NOTE]
> Never commit `.env` or plain-text credentials into version control.

---

## 6. How to Run the Server

From within the `backend/` directory with the virtual environment activated:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The application will be accessible at `http://localhost:8000`.

---

## 7. How to Run Tests

Run the test suite using `pytest`:

```bash
pytest
```

To run with verbose output:

```bash
pytest -v
```

Tests run with mocked database dependencies and do not require an active PostgreSQL instance.

---

## 8. API Documentation & Endpoints

Once the application is running, interactive API documentation is available at:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **OpenAPI JSON Schema:** [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

### Core Foundation Endpoints

- `GET /health` — Application health check (returns status and service identifier).
- `GET /health/db` — Live PostgreSQL connectivity check (returns `200 OK` on successful ping or `503 Service Unavailable` on database failure).

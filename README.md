# CI/CD Demo

A minimal Flask app for demonstrating a practical CI/CD pipeline with GitHub Actions, Docker, Docker Hub, and Render.

## Pipeline

```text
Push / Pull Request
        ↓
Test (pytest)
Lint (Ruff)
Security Scan (Bandit)
        ↓
Push to main
        ↓
Build Docker Image
        ↓
Push to Docker Hub
        ↓
Deploy to Render
```

## Run Locally
```
uv sync
uv run python -m cicd_demo.app
```

## Run Tests
```
uv run pytest -q
```

## Docker
```
docker build -t cicd-demo .
docker run --rm -p 8080:8080 cicd-demo
```

## Project Structure
```
src/
└── cicd_demo/
    ├── __init__.py
    └── app.py

tests/
└── test_app.py
```

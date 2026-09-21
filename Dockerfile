FROM python:3.12-slim

# Copy uv from the official uv image.
COPY --from=ghcr.io/astral-sh/uv:0.12.17 /uv /uvx /bin/

WORKDIR /app

# Install third-party dependencies first.
# This layer can be cached as long as dependency files do not change.
COPY pyproject.toml uv.lock README.md ./

RUN uv sync --locked --no-dev --no-install-project

# Copy the actual application package.
COPY src ./src

# Install the project itself.
RUN uv sync --locked --no-dev

# Use the virtual environment created by uv.
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8080

CMD ["sh", "-c", "exec gunicorn --bind 0.0.0.0:${PORT:-8080} cicd_demo.app:app"]
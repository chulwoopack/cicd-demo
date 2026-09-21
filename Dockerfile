FROM python:3.12-slim

WORKDIR /app

# Copy dependencies first so Docker can reuse this layer
# when application code changes.
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8080} app:app"]
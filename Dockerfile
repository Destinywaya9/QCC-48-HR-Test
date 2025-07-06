# Base image for backend (Python + FastAPI)
FROM python:3.11-slim AS backend

WORKDIR /app

COPY qcc_48h_demo_config.json ./
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

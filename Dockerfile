# stable, lightweight Python base image
FROM python:3.11-slim

# Set system environment optimizations
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Set the working directory inside the container

WORKDIR /app

# Install system-level dependencies if required by numerical libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first to optimize layer caching
COPY requirements.txt .

# Install dependencies directly into the container environment
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code (main.py, models, templates, etc.)
COPY . .

# Expose the network port your FastAPI app runs on
EXPOSE 8000

# Command to run your ASGI application using Uvicorn
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]


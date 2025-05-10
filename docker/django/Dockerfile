# Use a slim Python image
FROM python:3.11-slim

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Run Django via Gunicorn (production-ready WSGI server)
CMD ["gunicorn", "django_app.wsgi:application", "--bind", "0.0.0.0:8000"]

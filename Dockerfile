# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy file needed and setup work directory
COPY ./src /app/src
COPY ./app.py /app/
COPY ./Pipfile /app/

# Install Pipenv
RUN pip install -U pipenv

# Install dependencies using Pipenv
RUN pipenv install --deploy

# Expose port 8080 for Gunicorn
EXPOSE 8080

# Run Gunicorn
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8080", "app:app"]

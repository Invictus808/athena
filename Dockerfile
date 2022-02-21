# Pull official base image
FROM python:3.9.5-slim-buster

# Install system dependencies
RUN apt-get update \
    # && apt-get -y install netcat gcc postgresql \
    && apt-get clean \
    && adduser --disabled-password athena-api

# Set environment variables
ENV PATH="$PATH:/home/athena-api/.local/bin" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /tests

# Add tests
COPY ./src/tests/resources/. .

# Set working directory
WORKDIR /app

# Add application
COPY ./src/main/resources/. .
COPY ./requirements.txt .

# Change file permissions
RUN chown athena-api:athena-api -R /app \
    && chown athena-api:athena-api -R /tests

# Run as non-root user
USER athena-api

# Install requirements
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# Add entrypoint.sh
CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]

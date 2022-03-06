#!/bin/sh

echo "Waiting for PostgreSQL database container..."

while ! nc -z api-database 5432; do
    sleep 0.1
done

echo "PostgreSQL database container started."


echo "Starting Athena API"

python manage.py run -h 0.0.0.0
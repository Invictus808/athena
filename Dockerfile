# Pull official base image
FROM python:3.12.5-slim-bullseye AS base

# Set environment variables
ENV PATH="$PATH:/home/athena/.local/bin" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && apt-get clean \
    && python -m pip install --upgrade pip \
    && pip install poetry \
    && useradd -ms /bin/bash athena \
    && mkdir /athena/ /logs/

# Add documents and dependencies
COPY athena/__init__.py athena/__init__.py
COPY LICENSE poetry.lock pyproject.toml README.md /

# Change directory and file permissions
RUN chown athena:athena -R /athena/ /logs/ LICENSE poetry.lock pyproject.toml README.md

# Run as non-root user
USER athena

# Install application requirements
RUN poetry install --no-dev --no-interaction --no-ansi


# Pull official base image
FROM base AS production

# Set environment variables
ENV PATH="$PATH:/home/athena/.local/bin" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Add application
COPY athena/ /athena/

# Run application
CMD ["poetry", "run", "uvicorn", "athena.main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]

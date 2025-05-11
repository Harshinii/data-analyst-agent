# Use Python 3.11.9 slim as base image
FROM python:3.11.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

# Set the working directory
WORKDIR /app

# Install system dependencies for building Python packages and pyarrow
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    curl \
    git \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy Poetry files first (to leverage Docker cache)
COPY pyproject.toml poetry.lock* ./

# Install project dependencies (no local install)
RUN poetry install --no-root

# Optionally install additional Jupyter-related packages
RUN pip install ipykernel pandas numpy matplotlib seaborn statsmodels scipy scikit-learn

# Copy all project files
COPY . .

# Copy the environment file
COPY .env .env

# Command to run the application
CMD ["poetry", "run", "python", "src/newproj/main.py"]
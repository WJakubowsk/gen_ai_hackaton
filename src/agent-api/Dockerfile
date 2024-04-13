FROM python:3.11-slim

# Install required packages for Microsoft SQL Server
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gnupg \
 && curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc \
 && curl https://packages.microsoft.com/config/debian/10/prod.list | tee /etc/apt/sources.list.d/mssql-release.list \
 && apt-get update \
 && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql18 \
 && ACCEPT_EULA=Y apt-get install -y --no-install-recommends mssql-tools18 \
 && echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc \
 && apt-get install -y --no-install-recommends unixodbc-dev \
 && apt-get install -y --no-install-recommends libgssapi-krb5-2 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry==1.6.1

# Configure Poetry
RUN poetry config virtualenvs.create false

# Set working directory
WORKDIR /code

# Copy project files
COPY ./pyproject.toml ./README.md ./poetry.lock* ./

# Copy packages
COPY ./package[s] ./packages

# Install project dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Copy application code
COPY ./app ./app

# Install application dependencies
RUN poetry install --no-interaction --no-ansi

# Expose port
EXPOSE 8080

# Run the application
CMD exec uvicorn app.server:app --host 0.0.0.0 --port 8080

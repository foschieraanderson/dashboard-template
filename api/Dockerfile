FROM python:3.11-slim

# Set some global variables to be used across the Dockerfile
ARG WORKDIR="/www"
ARG APPNAME="app"

# Set the working directory to a secure non-root location
WORKDIR /home/${APPNAME}${WORKDIR}

# Configure Python to not buffer "stdout" or create .pyc files
ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Add and configure poetry to manage the dependencies
# Install Poetry
#RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
#    cd /usr/local/bin && \
#    ln -s /opt/poetry/bin/poetry && \
#    poetry config virtualenvs.create false

RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY ./pyproject.toml ./poetry.lock* /home/${APPNAME}${WORKDIR}/
#RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# # Install the runtime dependencies using pip
#RUN pip install --no-cache-dir --upgrade -r /home/${APPNAME}${WORKDIR}/requirements.txt
RUN bash -c "poetry install --no-root;"

# Copy the source code to the container
COPY . .

# Expose the port used by the application so that its accessible outside the container
EXPOSE 8000

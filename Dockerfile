FROM python:3.10-slim

ARG POETRY_HOME=/opt/poetry

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc curl

ENV PATH="${POETRY_HOME}/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python3 - --version 1.8.3

WORKDIR /src

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root --no-directory --only main

COPY physiopedia/ ./physiopedia/

RUN poetry install --only main

WORKDIR /src/physiopedia

EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"] 
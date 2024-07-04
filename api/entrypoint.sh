#!/bin/sh

# Executa as migrações do banco de dados
poetry run alembic upgrade head

# Inicia a aplicação
poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

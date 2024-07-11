#!/bin/sh

# Executa as migrações do banco de dados
alembic upgrade head

# Inicia a aplicação
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

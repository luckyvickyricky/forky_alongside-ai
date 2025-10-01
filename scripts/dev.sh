#!/bin/bash

cd "$(dirname "$0")/.."

if [ ! -f .env ]; then
    echo "Error: .env file not found"
    exit 1
fi

echo "Starting development server with hot reload..."
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000


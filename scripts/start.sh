#!/bin/bash

cd "$(dirname "$0")/.."

if [ ! -f .env ]; then
    echo "Error: .env file not found"
    exit 1
fi

echo "Starting Forky AI Interview Server..."
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4


#!/bin/bash

cd "$(dirname "$0")/.."

echo "Starting server in background..."
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 &
SERVER_PID=$!

sleep 3

echo "Running tests..."
uv run python test_server.py
TEST_RESULT=$?

echo "Stopping server..."
kill $SERVER_PID 2>/dev/null

exit $TEST_RESULT


#!/bin/bash

cd "$(dirname "$0")/.."

echo "Installing UV package manager..."
if ! command -v uv &> /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

echo "Installing dependencies..."
uv sync

echo "Installation complete!"
echo "Please configure your .env file before starting the server."


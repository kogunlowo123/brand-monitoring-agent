#!/bin/bash
set -euo pipefail
echo "Setting up Brand Monitoring Agent..."
pip install -e ".[dev]"
echo "Setup complete!"

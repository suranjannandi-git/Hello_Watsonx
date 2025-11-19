#!/bin/bash

echo "==============================================="
echo "      Setting up the app (Python)              "
echo "==============================================="

# Navigate to project root
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

##################################################
# 1. Create virtual environment IF NOT exists
##################################################
if [ ! -d "venv-dev" ]; then
    echo "[1/3] Creating Python virtual environment (venv-dev)..."
    python3.12 -m venv venv-dev
else
    # echo "[1/4] Virtual environment already exists. Skipping creation."
    echo -e "\e[33m[1/3] Virtual environment already exists. Skipping creation.\e[0m"

fi

##################################################
# 2. Activate virtual environment
##################################################
echo "[2/3] Activating virtual environment..."
# shellcheck source=/dev/null
source venv-dev/bin/activate || { echo "Failed to activate venv-dev"; exit 1; }

##################################################
# 3. Install dependencies
##################################################
echo "[3/3] Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "==============================================="
echo -e "\e[32mBackend setup completed. Starting backend server:\e[0m"
python call_wx_restapi.py
echo "==============================================="

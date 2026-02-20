#!/bin/bash

echo "🚀 Starting Financial Forensics Engine..."
echo "📁 Working directory: $(pwd)"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 first."
    exit 1
fi

# Check if the data file exists
if [ ! -f "data/money-muling.csv" ]; then
    echo "❌ Data file not found at data/money-muling.csv"
    echo "Please make sure the file exists."
    exit 1
fi

echo "📁 Data file found: data/money-muling.csv"
echo ""

# Start the server
python3 server.py

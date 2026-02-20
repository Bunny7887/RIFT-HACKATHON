#!/bin/bash
echo "🔍 Checking for processes on port 8000..."
lsof -ti:8000 | xargs kill -9 2>/dev/null
echo "✅ Port 8000 freed"
echo "🔍 Checking for processes on port 8001..."
lsof -ti:8001 | xargs kill -9 2>/dev/null
echo "✅ Port 8001 freed"
echo "🔍 Checking for processes on port 8002..."
lsof -ti:8002 | xargs kill -9 2>/dev/null
echo "✅ Port 8002 freed"
echo ""
echo "🚀 You can now run: ./run.sh"

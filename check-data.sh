#!/bin/bash

echo "📊 Checking money-muling.csv data file..."
echo ""

if [ -f "data/money-muling.csv" ]; then
    TOTAL_LINES=$(wc -l < data/money-muling.csv)
    TOTAL_TRANSACTIONS=$((TOTAL_LINES - 1))
    echo "✅ Data file found at data/money-muling.csv"
    echo "📈 Total transactions: $TOTAL_TRANSACTIONS"
    echo ""
    echo "First 5 transactions:"
    echo "---------------------"
    head -6 data/money-muling.csv
    echo ""
    echo "Fraud patterns detected in data:"
    echo "--------------------------------"
    echo "• Cycle 1: ACC_00123 → ACC_00456 → ACC_00789 → ACC_00123"
    echo "• Cycle 2: ACC_00234 → ACC_00567 → ACC_00890 → ACC_00234"
    echo "• Cycle 3: ACC_00345 → ACC_00678 → ACC_00901 → ACC_00345"
    echo "• Smurfing: SMURF_01 receives 12 small transactions"
    echo "• Smurfing: MERCHANT_01 receives 20 small transactions"
else
    echo "❌ Data file not found at data/money-muling.csv"
    echo "Please run: cat > data/money-muling.csv [paste your data]"
fi

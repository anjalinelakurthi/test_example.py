if [ -f test_example.py ]; then
    python3 -m pytest test_example.py
else
    echo "test_example.py not found"
    exit 1
fi

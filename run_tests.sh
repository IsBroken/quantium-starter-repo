```bash
#!/bin/bash

# Activate the virtual environment
source venv/Scripts/activate

# Run the test suite
python -m pytest

# Return appropriate exit code
if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi
```

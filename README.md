# mydsa

A lightweight Python package for testing and evaluating Data Structures and Algorithms (DSA) solutions.

## Features

- Evaluate multiple test cases
- Compare expected and actual outputs
- Useful for practicing coding interview and DSA problems

## Installation

### From GitHub

```bash
pip install git+https://github.com/yourusername/mydsa.git
```

## Usage

### Example Function

```python
def locate_card(cards, query):
    position = 0

    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1

    return -1
```

### Example Test Cases

```python
tests = [
    {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 7
        },
        'output': 3
    },
    {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 13
        },
        'output': 0
    }
]
```

### Running Tests

```python
from mydsa import evaluate_test_cases

evaluate_test_cases(locate_card, tests)
```

### Expected Output

```text
Test 1
Expected: 3
Actual: 3
PASS

Test 2
Expected: 0
Actual: 0
PASS
```

## Project Structure

```text
mydsa/
│
├── pyproject.toml
├── README.md
│
└── mydsa/
    ├── __init__.py
    └── testing.py
```

## Requirements

- Python 3.8 or higher

## Author

Muhammed Fazil

## License

MIT License

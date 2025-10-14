# ram-ai-python-learning

## Setup

### Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
# Upgrade pip first
pip install --upgrade pip
# Install package in editable mode
pip install -e ".[dev]"
```

## Running Tests
```bash
pytest tests/
# or using invoke
invoke test
```

## Available Tasks
```bash
invoke --list
```

- `invoke test` - Run tests
- `invoke format` - Format code
- `invoke lint` - Run linting checks
- `invoke clean` - Clean build artifacts
- `invoke install` - Install in development mode

## Docker

### Build and Run
```bash
docker build -t ram-ai-python .
docker run ram-ai-python
```

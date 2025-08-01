# Simple FastAPI Test App

A minimal FastAPI application for testing deployment with interconnected files.

## Project Structure

```
testrail/
├── main.py         # FastAPI app (calls file1)
├── file1.py        # Processes data (calls file2)  
├── file2.py        # Returns JSON response
├── requirements.txt # Dependencies
├── test_simple.py  # Test script
└── README.md       # This file
```

## How it works

1. **main.py** - FastAPI endpoint `/test` calls `file1.process_data()`
2. **file1.py** - Processes input and calls `file2.get_response_data()`
3. **file2.py** - Returns a JSON response

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
python main.py
```

3. Test endpoints:
- `http://localhost:8000/` - Hello message
- `http://localhost:8000/test` - Test the file chain
- `http://localhost:8000/health` - Health check
- `http://localhost:8000/docs` - API docs

## Test the file connections:
```bash
python test_simple.py
```

## For deployment:
This structure is perfect for testing FastAPI deployment on platforms like:
- Heroku
- Railway  
- Render
- Vercel
- AWS Lambda

Just ensure `main.py` is your entry point!

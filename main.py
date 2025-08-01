from fastapi import FastAPI
from file1 import process_data

app = FastAPI(title="Simple Test API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Hello from main.py"}

@app.get("/test")
def test_endpoint():
    # Main calls file1
    result = process_data("test input")
    return result

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


#check
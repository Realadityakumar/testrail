import json
from datetime import datetime

def get_response_data(data):
    """
    File2 returns a JSON response
    """
    print(f"File2: Received data - {data}")
    
    # Create a JSON response
    response = {
        "from_file2": True,
        "received_data": data,
        "timestamp": datetime.now().isoformat(),
        "status": "success",
        "data": {
            "id": 123,
            "name": "test_response",
            "value": "Hello from file2!",
            "processed": True
        }
    }
    
    return response

def get_simple_json():
    """
    Returns a simple JSON for testing
    """
    return {
        "message": "Simple response from file2",
        "status": "ok",
        "code": 200
    }

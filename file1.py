from file2 import get_response_data

def process_data(input_data):
    """
    File1 processes input and calls file2
    """
    print(f"File1: Processing input - {input_data}")
    
    # Call file2 to get response
    response = get_response_data(input_data)
    
    # Add some processing in file1
    final_result = {
        "from_file1": True,
        "processed_input": input_data,
        "file2_response": response,
        "message": "Data processed through file1 -> file2"
    }
    
    return final_result

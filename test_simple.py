"""
Simple test to verify the file connections work
"""

from file1 import process_data
from file2 import get_response_data, get_simple_json

def test_connections():
    print("Testing file connections...")
    print("=" * 50)
    
    # Test file2 directly
    print("1. Testing file2 directly:")
    result2 = get_response_data("direct test")
    print(f"   Result: {result2}")
    
    print("\n2. Testing file1 -> file2:")
    result1 = process_data("test from main")
    print(f"   Result: {result1}")
    
    print("\n3. Testing simple JSON:")
    simple = get_simple_json()
    print(f"   Result: {simple}")
    
    print("\n" + "=" * 50)
    print("All tests completed!")

if __name__ == "__main__":
    test_connections()

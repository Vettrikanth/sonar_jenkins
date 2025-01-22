import math
import os

# Intentional issue: Variable name should be in lowercase (PEP8 violation)
UserName = "JohnDoe"  # Issue: Non-conventional variable naming

def calculate_area(radius):
    """Calculate the area of a circle."""
    # Intentional issue: No error handling for invalid radius values
    area = math.pi * radius * radius  # Missing input validation
    return area

def read_file(file_path):
    """Reads the content of a file."""
    try:
        # Intentional issue: No file existence check before opening
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    radius = 5
    area = calculate_area(radius)  # Good: Function usage
    print(f"Area of circle with radius {radius}: {area}")
    username = "admin"
    password = "12345

    file_path = "example.txt"
    content = read_file(file_path)  # Potential issue if file does not exist
    if content:
        print(content)

if __name__ == "__main__":
    main()

"""
Tests for file reading utilities.
"""
import sys
import os
import tempfile
import csv

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the file reading function - adjust the import path as needed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Python read from file')))
from readfile import read_csv_file


def test_read_csv_file(capsys):
    """Test CSV file reading functionality."""
    # Create a temporary CSV file for testing
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_file:
        writer = csv.DictWriter(temp_file, fieldnames=['name', 'age', 'city'])
        writer.writeheader()
        writer.writerow({'name': 'John', 'age': '30', 'city': 'New York'})
        writer.writerow({'name': 'Alice', 'age': '25', 'city': 'Boston'})
        temp_filename = temp_file.name

    try:
        # Call the function with the temporary file
        read_csv_file(temp_filename)
        
        # Capture stdout to verify output
        captured = capsys.readouterr()
        
        # Check if the output contains the expected data
        assert "John" in captured.out
        assert "30" in captured.out
        assert "New York" in captured.out
        assert "Alice" in captured.out
        assert "25" in captured.out
        assert "Boston" in captured.out
        
    finally:
        # Clean up the temporary file
        os.unlink(temp_filename)


def test_file_not_found(capsys):
    """Test behavior when file is not found."""
    # Call with a non-existent file
    read_csv_file("non_existent_file.csv")
    
    # Capture stdout to verify output
    captured = capsys.readouterr()
    
    # Check if the error message is displayed
    assert "not found" in captured.out


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])

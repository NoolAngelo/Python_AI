"""
File utilities for reading and processing different file formats.

This module provides functions for reading and processing various file formats
including CSV files.
"""
import csv
import sys
from typing import Dict, List, Any, Optional, Iterator


def read_csv_file(filename: str) -> None:
    """
    Reads and prints the contents of a CSV file.
    
    Args:
        filename (str): Path to the CSV file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        Exception: For any other errors encountered while reading the file.
    """
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def parse_csv_to_dict(filename: str) -> List[Dict[str, Any]]:
    """
    Reads a CSV file and returns its contents as a list of dictionaries.
    
    Args:
        filename (str): Path to the CSV file.
    
    Returns:
        List[Dict[str, Any]]: A list of dictionaries where each dictionary
                             represents a row from the CSV file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    result = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                result.append(dict(row))
        return result
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")


def csv_to_generator(filename: str) -> Iterator[Dict[str, str]]:
    """
    Creates a generator that yields rows from a CSV file as dictionaries.
    
    This is memory efficient for large CSV files as it reads one row at a time.
    
    Args:
        filename (str): Path to the CSV file.
    
    Yields:
        Dict[str, str]: A dictionary representing a row from the CSV file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield dict(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")


def main() -> int:
    """
    Command-line interface for reading CSV files.
    
    Returns:
        int: Exit code (0 for success, 1 for error)
    """
    if len(sys.argv) != 2:
        print("No file provided as argument.")
        filename = input("Please enter the CSV filename: ")
    else:
        filename = sys.argv[1]
    
    try:
        read_csv_file(filename)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

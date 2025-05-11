import csv
import sys

def read_csv_file(filename):
    """
    Reads and prints the contents of a CSV file.
    
    Args:
        filename (str): Path to the CSV file.
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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("No file provided as argument.")
        filename = input("Please enter the CSV filename: ")
    else:
        filename = sys.argv[1]
    
    read_csv_file(filename)
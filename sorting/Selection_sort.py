def selection_sort(numbers):
    """
    Sorts a list using the Selection Sort algorithm.
    
    Args:
        numbers (list): List of numbers to be sorted.
    
    Returns:
        list: Sorted list.
    """
    length = len(numbers)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

# Interactive example usage
if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = list(map(int, user_input.split()))
        sorted_numbers = selection_sort(numbers)
        print("Sorted numbers:", sorted_numbers)
    except ValueError as e:
        print(f"Error: {e}")

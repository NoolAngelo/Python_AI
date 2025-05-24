def quick_sort(arr):
    """
    Sorts a list using the Quick Sort algorithm.

    Args:
        arr (list): List of numbers to be sorted.

    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


# Interactive example usage
if __name__ == "__main__":
    try:
        user_input = input("Enter array numbers separated by space: ")
        array = list(map(int, user_input.split()))
        print("Length of the array:", len(array))
        print("Unsorted array:", array)
        print("Sorted array:", quick_sort(array))
    except ValueError as e:
        print(f"Error: {e}")

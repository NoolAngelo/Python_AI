def merge_sort(arr):
    """
    Sorts a list using the Merge Sort algorithm.

    Args:
        arr (list): List of numbers to be sorted.

    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left (list): Left half of the list.
        right (list): Right half of the list.

    Returns:
        list: Merged sorted list.
    """
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Interactive example usage
if __name__ == "__main__":
    try:
        user_input = input("Enter numbers for the test case (comma-separated): ")
        arr = list(map(int, user_input.split(",")))
        print("Unsorted List:", arr)
        print("Sorted List:", merge_sort(arr))
        if (len(arr) % 2) == 0:
            print("The array is even")
        else:
            print("The array is odd")
    except ValueError as e:
        print(f"Error: {e}")

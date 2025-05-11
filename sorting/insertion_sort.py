def insertion(list_a):
    """
    Sorts a list using the Insertion Sort algorithm.
    
    Args:
        list_a (list): List of numbers to be sorted.
    
    Returns:
        list: Sorted list.
    """
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i>0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i-1
    return list_a

# Interactive example usage
if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        list_a = [int(num) for num in user_input.split()]
        result = insertion(list_a)
        print("Sorted values:", result)
    except ValueError as e:
        print(f"Error: {e}")

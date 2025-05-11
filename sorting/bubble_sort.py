def bubble(list_a):
    """
    Sorts a list using the Bubble Sort algorithm.
    
    Args:
        list_a (list): List of numbers to be sorted.
    
    Returns:
        list: Sorted list.
    """
    index_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a

# Interactive example usage
if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        list_a = [int(num) for num in user_input.split()]
        result = bubble(list_a)
        print("Numbers in order:", result)
    except ValueError as e:
        print(f"Error: {e}")

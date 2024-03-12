def merge_sort(lst):
    # Base case: if the list is empty or has only one element, it's already sorted
    if len(lst) <= 1:
        return lst

    # Split the list into two halves
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Merge the two lists by taking the smallest element from either list at each step
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in either list, add them to the merged list
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def main():
    lst = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = merge_sort(lst)
    print("Original List:", lst)
    print("Sorted List:", sorted_list)

if __name__ == "__main__":
    main()
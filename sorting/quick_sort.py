def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

user_input = input("enter array numbers separated by space: ")
array = list(map(int,user_input.split()))

print("length of the array: ",len(array))
print("unsorted array: ",array)
print("sorted array: ",quick_sort(array))

# 1. Basic sort function
def basic_sort(arr):
    return sorted(arr)

# 2. Sort in descending order
def sort_descending(arr):
    return sorted(arr, reverse=True)

# 3. Sort by length of elements
def sort_by_length(arr):
    return sorted(arr, key=len)

# 4. Sort by second element of tuple
def sort_by_second_element(arr):
    return sorted(arr, key=lambda x: x[1])

# 5. Sort by last character of string
def sort_by_last_char(arr):
    return sorted(arr, key=lambda x: x[-1])

# 6. Sort by absolute value
def sort_by_absolute_value(arr):
    return sorted(arr, key=abs)

# 7. Sort by frequency of elements
def sort_by_frequency(arr):
    return sorted(arr, key=arr.count)

# 8. Sort a list of dictionaries by a common key
def sort_dict_by_key(arr, key):
    return sorted(arr, key=lambda x: x[key])

# 9. Sort a list of objects by an attribute
def sort_objects_by_attribute(arr, attr):
    return sorted(arr, key=lambda x: getattr(x, attr))

# 10. Sort a list of strings ignoring case
def sort_strings_ignore_case(arr):
    return sorted(arr, key=lambda x: x.lower())
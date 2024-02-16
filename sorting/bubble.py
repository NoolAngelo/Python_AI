def bubble():
    index_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a

user_input = input("enter nmumbers separated by spaces: ")
list_a = [int(num) for num in user_input.split()]

result = bubble()
print("numbers in order : ", result)


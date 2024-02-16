numbers = [55, 94, 42, 22, 11, 90]
length = len(numbers)

for i in range(length):
    min_index = i
    for j in range(i + 1, length):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]  # swap should be here

print(numbers)

def sayhi(name):
    print("Hello boss:" , name)

user_input = input("input name: ")
sayhi(user_input)

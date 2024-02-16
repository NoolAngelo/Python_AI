numbers = [54,54,65,45,345,25,234]
length = len(numbers)

for i in range(length):
    min_index =i
    for j in range(i+1, length):
        if numbers[min_index] > numbers[j]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
print(numbers)
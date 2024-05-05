counter = 0
my_list = []

while counter < 10:
    number = int(input("Enter a number: "))
    my_list.append(number)
    counter += 1

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print("Even numbers:", new_list)


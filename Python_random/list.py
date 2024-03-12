friends = ["Kalbo","Kinis","Kintab"]
user_input = int(input("input the range of the list: " ))
print("existing values in a list:")
print(friends)

for i in range(user_input):
    added = input("Enter a string to add to the list: ")
    friends.append(added)
    print(friends)

    print("the length of the lis is:"),print(len(friends))

coordinates = (4,5)
print(coordinates)
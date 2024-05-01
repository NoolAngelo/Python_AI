import time

name ="Nool/Angelo"

first_name = name[:4]
last_name = name[5:]
funky_name = name[0:11:3]
reversed_name = name[::-1]

slice = slice(4,-2)

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

print(name[slice])


for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("bomba na!")

food = ["pizza","burger","hotdog","pudding"]
food[0] = "bomba na"

food.append("ice cream")
food.remove("burger")
food.pop()
food.insert(1,"cake")
food.sort()

for x in food:
    print(x)

drinks = ["coffee","soda","tea"]
dinner = ["adobo","sinigang","tinola"]
dessert = ["makapuno ice cream", "tubeg","mango"]
food1 =[drinks,dinner,dessert]
print(food1[2][2])
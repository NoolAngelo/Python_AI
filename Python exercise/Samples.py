import time
#1st sample
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

#2nd sample
for seconds in range(3,0,-1):
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

#3rd sample
utensils = {"fork","spoon","knife"}
dishes = {"pan","bowl","cup"}

utensils.add("napkins")
utensils.update(dishes)
dinner_table = utensils.union(dishes)

for task in dinner_table:
    print(task)
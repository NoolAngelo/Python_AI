def add_two_num(num1,num2):
    result = num1+num2
    return result

num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))

print("the sum: ", add_two_num(num1,num2))

def absolute_value(num):
    """returns the absolute value of entered num"""
    if num>=0:
        return num
    else:
        return -num

print(absolute_value(5))
print(absolute_value(-4))
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
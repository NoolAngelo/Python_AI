
capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'Philippines':'Manila',
            'Russia':'Moscow'}


print(capitals['Philippines'])
print(capitals.get('Russia'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for x,y in capitals.items():
    print(x,y)
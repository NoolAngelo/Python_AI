x = 5

def sample():
    x = 10
    print("local x:", x)

sample()
print("global x: ", x)

def money():
    x = "money ko!"

    def alkansya():
        nonlocal x
        x="non local"
        print("inner", x)

    alkansya()
    print("outer", x)
money()
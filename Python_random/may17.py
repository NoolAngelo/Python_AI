class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoIsThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

    def run(self):
        print("Run faster")


class Penguin(Bird):
    def __init__(self):
        super().__init__()  # call the parent's init method
        print("Penguin is ready")

    def whoIsThis(self):
        print("Penguin")

    def run(self):
        super().run()  # call the parent's run method
        print("Run faster2")


class Bat(Penguin):
    def __init__(self):
        super().__init__()  # call the parent's init method
        print("Bat is ready")

    def flyhigh(self):
        print("So high")


pegg = Penguin()
pegg.whoIsThis()
pegg.swim()
pegg.run()
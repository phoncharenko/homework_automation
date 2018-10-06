class Person:
    title = "human"

    def __init__(self, n=""):
        self.name = n

    def printer(self):
        print(self.title)

    def set_name(self, n):
        self.name = n


if __name__ == "__main__":
    p1 = Person()
    p2 = Person("Vasya")

    print(p1.name)
    print(p2.name)

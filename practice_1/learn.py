class Person:

    def __init__(self, name='', surname='', age=0):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):
        return self.name + ' ' + self.surname

    def get_older(self, years):
        return self.age + years

    def __str__(self):
        return "<Person object: name = {} {}>".format(self.name, self.surname)


if __name__ == "__main__":
    p1 = Person("Vasya", "Petrenko", 10)
    print(p1)
    print(p1.full_name(), p1.get_older(20))

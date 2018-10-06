from practice_1.learn import Person


class EmployeeInfopulse(Person):
    def __init__(self, name='', surname='', age=10, position=None, salary=''):
        Person.__init__(self, name, surname, age)
        self.position = position
        self.salary = salary

    def income(self, month):
        return self.salary * month


if __name__ == "__main__":
    e1 = EmployeeInfopulse(name='Olena', position="AutoQA", salary=1000)
    print(e1.name, e1.surname)
    print(e1)
    print(e1.age)
    print(e1.income(12))
    print(e1.salary)

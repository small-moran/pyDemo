class Employee(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # self._Employee__age  = age

    @property
    def salary(self):
        print("salary run......")
        return 10000

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


e1 = Employee("tom", 18)

print(e1.name)
# print(e1._Employee__age)
print(dir(e1))

print(e1.salary)

print(e1.age)
e1.age = 20
print(e1.age)

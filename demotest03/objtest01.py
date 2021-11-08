class Person:
    sex = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("Say hello!!!")

    def eat(self):
        print("eat delicious food!!!")

    def __str__(self):
        print("override的str")


class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score

    def eat(self):
        print("Student eat good!!!")


s1 = Student("tom", 18, 99)
s1.say()
s1.eat()
print(Student.mro())


def eatFood(person):
    if isinstance(person, Person):
        person.eat()
    else:
        print("no food ")


eatFood(Student("tom", 18, 99))
eatFood(Person("jack", 20))

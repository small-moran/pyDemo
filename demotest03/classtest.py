class Student:
    school = "bilibili"

    @classmethod
    def printSchool(cls):
        print("学校是：", cls.school)

    def __init__(self, name, ege, score):
        self.name = name
        self.ege = ege
        self.score = score

    def put_score(self):
        print(f"{self.name}的成绩为{self.score}")


def play_game(s):
    print(f"{s}在玩游戏")


s1 = Student("spike", 18, 88)
s1.put_score()
Student.put_score(s1)

print(s1.__dict__)  # 获得属性字典

Student.printSchool()

s1.printSchool()

Student.play = play_game
s1.play2 = play_game

print(s1)

s1.play()
# 等价于
Student.play(s1)

s1.play2("tom")

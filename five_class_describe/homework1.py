# -*- coding:utf-8 -*-
class Dog:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def bark(self):
        anger = self.size / 10
        if anger > 10:
            print("它会叫")
        else:
            print("不会叫")


class House:
    def __init__(self, style, size, position):
        self.style = style
        self.size = size
        self.position = position

    def price(self, unit):
        reference_price = self.size * unit
        print(f"房屋参考价格为{reference_price/10000}万")


class Teacher:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def character(self):
        if self.name == "AD" and self.gender == "female":
            print(f"{self.name}老师性格nice，声音好听，才没有{self.age}岁，一定只有18岁")
        else:
            print("其他老师也很好，嘿嘿")


class Work:
    def __init__(self, industry, years):
        self.industry = industry
        self.years = years

    def style(self, time, days):
        if time * days > 80:
            print("福报")
        else:
            print("不饱和")
        return "这是个好工作"


class School:
    def __init__(self, *args):
        self.name = args[0][0]
        self.schoolmaster = args[0][1]
        self.year = args[1][0]

    def score(self, xishu, renshu):
        score = xishu * renshu + self.year
        print(score)


if __name__ == "__main__":
    big_dog = Dog("black", 200)
    big_dog.bark()
    my_house = House("Northern Europe", 101, "深圳南山区")
    print(my_house.position)
    my_house.price(80000)
    my_teacher = Teacher("AD", "female", 25)
    my_teacher.character()
    print(Work("IT", 7).style(12, 7))
    list1 = ["hogwarts", "sihan"]
    list2 = [2]
    my_school = School(list1, list2)
    print(f"我的学校名字是{my_school.name}，我们的校长是{my_school.schoolmaster}，学校成立了{my_school.year}年")
    my_school.score(0.9, 1000)

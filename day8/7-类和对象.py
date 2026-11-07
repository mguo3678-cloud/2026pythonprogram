# 作者: 学不会
# 2026年10月13日20时36分55秒
# xxx@qq.com

# 定义一个类
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print(id(self))
        print(f"{self.name} is running")

    def eat(self):
        print(f"{self.name} is eating")


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print(f"{self.name} is barking")

    def wagging_tail(self):
        print(f"{self.name} is wagging tail")


def main():
    tiger = Person("老虎", 23, 175)
    tiger.run()
    tiger.eat()
    dog = Dog("旺财", "黄色")
    dog.bark()
    dog.wagging_tail()
    print(dir(tiger))


def test():
    tiger = Person("老虎", 23, 175)
    print(id(tiger))
    tiger.age = 19
    print(id(tiger))


def test2():
    tiger = Person("老虎", 23, 175)
    print(id(tiger))
    tiger.run()


if __name__ == '__main__':
    # main()
    # test()
    test2()

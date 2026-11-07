# 作者: 学不会
# 2026年10月15日14时24分20秒
# xxx@qq.com
class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print(f"{self.name} is playing")


class XiaoTianDog(Dog):
    def game(self):
        print(f"{self.name} is playing with a ball")


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self):
        print(f"{self.name}和{dog.name}一起玩")

if __name__ == '__main__':
    dog = Dog('旺财')
    dog.game()

    xtdog = XiaoTianDog('哮天犬')
    xtdog.game()

    xiaoming = Person('小明')
    xiaoming.game_with_dog()



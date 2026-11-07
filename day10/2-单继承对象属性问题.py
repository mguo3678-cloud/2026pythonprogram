# 作者: 学不会
# 2026年10月15日15时27分36秒
# xxx@qq.com
class Animal:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("叫-----")


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # 调用父类的构造函数
        self.color = color


if __name__ == '__main__':
    dog = Dog("旺财", "黄色")
    print(dog.name)  # 输出旺财
    print(dog.color)

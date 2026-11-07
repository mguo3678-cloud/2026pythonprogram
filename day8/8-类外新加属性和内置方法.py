# 作者: 学不会
# 2026年10月13日21时02分28秒
# xxx@qq.com

class Cat:
    def __init__(self):
        self.name = None

        self.weight = 3

    # 哪一个对象调用的方法，self就是哪一个对象的引用
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)

    def __str__(self):
        """
        重写str方法，返回对象的描述信息
        :return:
        """
        return f'{self.name}--{self.weight}'
    def __del__(self):
        print(self.name + "对象被销毁了")
cat = Cat()
cat.name = "小花"
cat.eat()
print(cat)
del cat
print("程序结束了")
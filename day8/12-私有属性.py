# 作者: 学不会
# 2026年10月14日12时45分57秒
# xxx@qq.com

class Person:
    def __init__(self, name):
        self.name = name  # 公有属性
        self.__age = 18  # 私有属性

    def get_age(self):
        return self.__age


xiaoli = Person('xiaoli')
print(xiaoli.get_age())

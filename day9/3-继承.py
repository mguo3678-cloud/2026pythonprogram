# 作者: 学不会
# 2026年10月15日14时22分36秒
# xxx@qq.com
class Animal:
    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Cat(Animal):
    # 子类拥有父类的所有属性和方法

    def catch(self):
        print("抓老鼠")


class Dog(Animal):
    def bark(self):
        print("汪汪---")


class XiaoTianQuan(Dog):
    def fly(self):
        print("在天上飞---")

    def bark(self):
        print("一直叫")
        super().bark()


if __name__ == '__main__':
    wangcai = Dog()
    wangcai.eat()
    xiaotianquan = XiaoTianQuan()
    xiaotianquan.fly()
    xiaotianquan.bark()

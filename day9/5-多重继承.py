# 作者: 学不会
# 2026年10月15日14时24分11秒
# xxx@qq.com

class A:
    def test(self):
        print('A test')

    def demo(self):
        print('A demo')


class B:
    def test(self):
        print('B test')

    def demo(self):
        print('B demo')


class C(A, B):
    pass


c = C()
c.test()#从第一个继承的类开始找，如果找不到就继续找下一个继承的类，直到找到为止。如果找不到就报错。
c.demo()
c.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# C.__mro__表示C的继承顺序，从左到右依次是C、A、B、object，object是所有类的父类，表示所有类的共同父类。

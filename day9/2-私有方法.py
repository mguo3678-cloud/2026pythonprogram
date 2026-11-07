# 作者: 学不会
# 2026年10月15日14时22分20秒
# xxx@qq.com
class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print(self.__age)

    def show_secret(self):
        self.__secret()


if __name__ == '__main__':
    xiaohong = Women('xiaohong')
    # AttributeError: 'Women'object hasno attribute'__secret'
    # xiaohong.__secret()  # 私有方法不能直接调用
    # print(xiaohong.__age)  # 私有属性不能直接调用
    # 绕过机制，但是不推荐
    xiaohong._Women__secret()  # 通过绕过机制调用私有方法
    print(xiaohong._Women__age)  # 通过绕过机制调用私有属性
    xiaohong.show_secret()

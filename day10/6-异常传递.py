# 作者: 学不会
# 2026年10月15日17时05分32秒
# xxx@qq.com

# def demo1():
#     num =int(input("请输入一个数字: "))
#     ret=10/num
#     print(ret)
#
# def demo2():
#     demo1()
#     print("demo2的代码已经执行")
#
# try:
#     demo2()
# except Exception as e:
#     print("捕获到异常:",e)

def demo1():
    return int(input("输入整数："))
def demo2():
    return demo1()
# 利用异常的传递性，在主程序捕获异常
try:
    print(demo2())
except Exception as result:
    print("未知错误 %s" % result)

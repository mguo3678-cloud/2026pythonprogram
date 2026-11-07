# 作者: 学不会
# 2026年10月13日19时33分42秒
# xxx@qq.com

def demo1(num1, *args, **kwargs):
    print(num1)
    print(args)
    print(kwargs)


def demo(num, *agrs, **kwargs):
    print(num)
    print(agrs)#args拿到了所有的位置参数
    print(kwargs)#kwargs拿到了所有keyword参数
    print('-' * 50)
    # *(2,3,4,5)变为2,3,4,5，**{'name':'小明'，'age':18,'gender':True},
    # 变为name="小明"，age=18,gender=True
    demo1(*agrs, **kwargs)


# demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)
my_tuple = (1, 2, 3, 4)
demo(*my_tuple, name="小明", age=18, gender=True)
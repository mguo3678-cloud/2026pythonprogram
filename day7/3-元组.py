# 作者: 学不会
# 2026年10月11日19时53分31秒
# xxx@qq.com

def test():
    return 1,2,3

ret=test()
print(ret)
print(type(ret))
# 元组转列表
list_ret=list(ret)
print(list_ret)

# 列表转元组
tuple_ret=tuple(ret)
print(tuple_ret)

# 元组生成式
a = tuple(x for x in range(10))
print(a)
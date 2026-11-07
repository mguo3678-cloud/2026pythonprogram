# 作者: 学不会
# 2026年10月12日17时34分31秒
# xxx@qq.com
# 切片
test_list = [1, 2, 3, 4, 5, 6]
test_list.insert(3, ['x', 'y', 'z'])  # 与下面的方法不同
# test_list[3:3]=['x','y','z']
print(test_list)

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # T
print(a is b)  # F

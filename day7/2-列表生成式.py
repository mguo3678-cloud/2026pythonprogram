# 作者: 学不会
# 2026年10月11日18时36分33秒
# xxx@qq.com

# 列表生成式
a = [x for x in range(10)]
print(a)

b = []
for i in range(10):
    b.append(i)
print(b)
# 理解两层for循环的列表生成式
a = [j for i in range(10) for j in range(i)]
print(a)

# 二维列表
a = [[col * row for col in range(5)] for row in range(5)]
print(a)

# 二维变一维
b = [j for i in a for j in i]
print(b)

# 只有if时
a = [x for x in range(10) if x % 2 == 0]  # 将只会筛选偶数
print(a)

# if-else 的三元表达式
a = [x if x % 2 == 0 else x ** 2 for x in range(10)]
print(a)

# 列表的简写
a = [1, 2, 3, 4, 5]
b = [2, 3, 4]
print(a + b)
a += b # a的id不会变
print(a)  # 等价于extend ,和a=a+b是不一样的

a = [1, 2, 3, 4, 5]
a = a + b  # a的id会变
print(a)

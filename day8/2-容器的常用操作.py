# 作者: 学不会
# 2026年10月12日19时13分48秒
# xxx@qq.com

# zip的作用是把两个元组进行对应位置进行匹配
a = (1, 2, 3)
b = ('a', 'b', 'c')
print(list(zip(a, b)))
print(dict(zip(a, b)))

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

#enumerate作用是把一个可迭代对象进行索引，返回一个索引和元素的元组
list1=list(enumerate(seasons))
print(list1)
dict1=dict(enumerate(seasons))
print(dict1)
#反转键值
dict2={v:k for k,v in dict1.items()}
print(dict2)
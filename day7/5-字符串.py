# 作者: 学不会
# 2026年10月12日14时16分33秒
# xxx@qq.com
str1 = "Hello Python"
for c in str1:
    print(c)

print(str1.count('l'))
print(str1.index('l'))
print(str1[4])

str2 = "Hello Hello Python".replace('Hello', 'Hi', 1)  # 只替换第一个Hello,默认替换所有

print(str2)

# split()方法,返回一个列表
str_list = "Hello Python".split(' ')
print(str_list)

# join()方法,将列表中的元素用指定的字符串连接起来
str3 = ' '.join(str_list)
print(str3)

# splitlines()方法,将字符串按行分割成列表
str4 = 'hello python\nworld\nhow\nare\nyou\ntoday'
print(str4.strip())
print(str4.splitlines())


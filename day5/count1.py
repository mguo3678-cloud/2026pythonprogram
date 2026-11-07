# 作者: 学不会
# 2026年10月09日20时27分52秒
# xxx@qq.com
# 计算数字二进制中1的个数
num = int(input("请输入一个数字:"))
print(bin(num).count('1'))
print(num.bit_count())
count = 0
while num > 0:
    count += num % 2
    num = num // 2
print(count)

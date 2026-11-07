# 作者: 学不会
# 2026年10月19日10时43分17秒
# xxx@qq.com


# 258. 各位相加
#
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

def addDigits(num):
    while num >= 10:
        ret = 0
        while num:
            ret += num % 10
            num = num // 10
        num = ret
    return num


# 202快乐数
def ishappy(num):
    # 会死循环
    # flag = False
    # while True:
    #     ret = 0
    #     ret += (num % 10) ** 2
    #     num = num // 10
    #     if ret == 1:
    #         flag = True
    #         break
    # return flag
    seen = set()  # 记录出现过的数
    while num not in seen and num != 1:
        seen.add(num)
        ret = 0
        while num:
            ret += (num % 10) ** 2
            num = num // 10
        num = ret
    return num == 1


# 1295. 统计位数为偶数的数字
def findNumbers(nums):
    ret = 0
    for num in nums:
        count = 0
        while num:
            count += 1

            num //= 10
        if count % 2 == 0:
            ret += 1
    return ret


# 728. 自除数
def selfDividingNumbers(left, right):
    result = []
    for num in range(left, right + 1):
        mid_num = num
        flag = True
        while mid_num:
            ret = mid_num % 10
            if ret == 0 or num % ret != 0:
                flag = False
                break
            mid_num //= 10

        if flag:
            result.append(num)
    return result


# 70 爬楼梯  #递归会超时
def climbStairs(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# 1837. K 进制表示下的各位数字总和
def sumBase(n, k):
    ret = 0
    while n:
        ret += n % k
        n //= k
    return ret


import math


# 7.整数反转
def num_reverse(x):
    mid_x=abs(x)
    rev=0
    while mid_x:
        ret=mid_x%10
        mid_x//=10
        rev=rev*10+ret
    if x<0:
        return -rev
    return rev

#9.回文数
def isPalindrome(x):
    INT_MIN,INT_MAX =-2**31, 2 ** 31 - 1
    #负数不是回文数
    if x<0:
        return False
    mid_x=x
    rev=0
    while mid_x:
        ret =mid_x%10
        mid_x//=10
        if rev>(INT_MAX-ret)//10:
            return False
        rev=rev*10+ret
    return x==rev


if __name__ == '__main__':
    # addDigits(38)
    # ishappy(19)
    # findNumbers([12, 345, 2, 6, 7896])
    # selfDividingNumbers(1, 22)
    # climbStairs(3)
    # sumBase(34, 6)
    # num_reverse(123)

    print(isPalindrome(123))
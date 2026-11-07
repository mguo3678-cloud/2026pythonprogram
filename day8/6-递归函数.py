# 作者: 学不会
# 2026年10月13日19时58分04秒
# xxx@qq.com

import sys

sys.setrecursionlimit(10000)  # 设置递归深度，防止栈溢出


def sum_fun(n):
    if n == 1:
        return 1
    return n + sum_fun(n - 1)


def step(n):
    if n == 1 or n == 2:
        return n
    return step(n - 1) + step(n - 2)


if __name__ == '__main__':
    # print(sum_fun(5))
    while True:
        try:
            n = int(input("请输入一个整数: "))
            print(step(n))
        except ValueError:
            print("输入无效，请输入一个整数。")
            continue
        except RecursionError:
            print("递归深度过深，请输入一个较小的整数。")
            continue
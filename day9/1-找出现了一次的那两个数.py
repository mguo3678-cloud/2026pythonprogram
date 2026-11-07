# 作者: 学不会
# 2026年10月15日13时23分22秒
# xxx@qq.com


def split_list(my_list):
    ret = 0
    for i in my_list:
        ret ^= i
    split_flag = ret & (-ret)
    ret1 = 0
    ret2 = 0
    ret1_list = []
    ret2_list = []
    for i in my_list:
        if i & split_flag:
            ret1 ^= i
            ret1_list.append(i)
        else:
            ret2 ^= i
            ret2_list.append(i)
    print(ret1, ret2)
    print(ret1_list)
    print(ret2_list)


if __name__ == '__main__':
    my_list = [1, 1, 2, 2, 3, 6, 6, 8, 3, 9, 8, 10]
    split_list(my_list)

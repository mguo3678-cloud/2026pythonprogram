# 作者: 学不会
# 2026年10月23日18时26分53秒
# xxx@qq.com

# 位图

def bit_map(my_list):
    int_bit_map = 0
    result = []
    for i in my_list:
        if int_bit_map & 1 << i + 100:  # 为真，表示已经出现过
            pass
        else:
            int_bit_map = int_bit_map | 1 << i + 100
            result.append(i)
    return result


if __name__ == '__main__':
    list1 = [95, 17, 3, 31, 86, 75, 56, 19, 38, 26,
             94, 54, 53, 72, 59, 61, 74, -58, 78, 60,
             64, 43, 52, 90, 84, 19, 92, 2, 71, 12,
             67, 10, 53, 85, 98, 24, 11, 41, 44, 55,
             10, 47, 43, 98, 9, 55, 18, 30, 44, 22,
             48, 15, 87, 28, 47, 18, 92, 3, 38, 87, 59,
             84, 76, 65, 82, 26, 47, 52, -58, 79, 50, 82,
             5, 71, 28, 30, 17, 51, 11, 58, 12, 54, 49, 73,
             24, 46, 99, 94, 93, 70, 12, 33, 19, 67, 62, 74, 61, 89,
             91, 51]
    print(bit_map(list1))
    print(len(bit_map(list1)))
    print('*'*50)
    print(set(list1))
    print(len(set(list1)))

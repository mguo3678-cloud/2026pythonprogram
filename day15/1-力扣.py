# 作者: 学不会
# 2026年10月26日13时27分01秒
# xxx@qq.com
# 1768.交替合并字符串

def merge_str(str1, str2):
    res = '' * (len(str1) + len(str2))
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        res += str1[i]
        res += str2[j]
        i += 1
        j += 1
    while i < len(str1):
        res += str1[i]
        i += 1
    while j < len(str2):
        res += str2[j]
        j += 1
    return res


# 389.找不同
def find_dif(s, t):
    # for i in t:
    #     if t.count(i)>s.count(i):
    #         return i

    # 集合
    # for i in set(t):
    #     if t.count(i) > s.count(i):
    #         return i

    # 字典
    # count = {}
    # for i in s:
    #     count[i] = count.get(i, 0) + 1
    # for i in t:
    #     if i not in count or count[i] == 0:
    #         return i
    #     count[i] -= 1

    # 位运算
    ans = 0
    for i in s + t:
        ans ^= ord(i)
    return chr(ans)


# 28.找出字符串中第一个匹配项的下标
def strStr(haystack, needle):
    return haystack.find(needle)  # 返回第一个匹配项的下标，如果没有匹配项，返回-1


# 242.有效的字母异位词
def isAnagram(s, t):
    return sorted(s) == sorted(t)


def shuffle(nums, n):
    ans = [0] * n * 2
    for i in range(n):
        ans[i*2] = nums[i]
        ans[i*2 + 1] = nums[i + n]
    return ans


if __name__ == '__main__':
    # str1 = 'abc'
    # str2 = 'pqr'
    # print(merge_str(str1, str2))  # 输出: 'apbqcr'
    # s = "abcd"
    # t = "abcde"
    # print(find_dif(s, t))
    # print(strStr('hello', 'llo'))
    # print(isAnagram('anagram', 'nagaram'))  # 输出: True
    # print(isAnagram('rat', 'car'))  # 输出: False
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(shuffle(nums, n))  # 输出: [2, 3, 5, 4, 1, 7]
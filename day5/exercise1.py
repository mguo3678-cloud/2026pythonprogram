# 作者: 学不会
# 2026年10月09日20时58分03秒
# xxx@qq.com
"""
1480.一维数组的动态和

给你一个数组nums。数组「动态和」的计算公式为：runningSum[i]=sum(nums[0]....nums[i])。
请返回nums的动态和。
示例 1：

输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
"""
nums = list(range(10))
#
# print(nums)
# def runningSum():
#     #原地修改数组
#     for i in range(1, len(nums)):
#         nums[i] += nums[i - 1]
#     return nums
#
#
# print(runningSum())

#1929. 数组串联
# 给你一个整数数组 nums ，请你返回 nums 的串联。
# 串联的意思是将所有数组元素连接成一个数组。

# nums =nums+nums
# nums.extend(nums)

def getConcatenation():
    n = len(nums)
    ans = [0] * 2 * n
    for i in range(0, len(nums)):
        ans[i] = nums[i]
    for i in range(len(nums), n):
        ans[i] = nums[i - (len(nums))]
    return ans

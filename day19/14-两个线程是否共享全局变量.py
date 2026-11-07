# 作者: 学不会
# 2026年11月03日19时33分51秒
# xxx@qq.com
from threading import Thread
import time

# # 全局变量
# g_num = 0
#
# def work1():
#     global g_num
#     for i in range(3):
#         g_num += 1
#
#     print("----in work1, g_num is %d---"%g_num)
#
#
# def work2():
#     global g_num
#
#
#     print("----in work2, g_num is %d---" % g_num)
#
# print(f'线程创建前，g_num的值是{g_num}')
# t1 = Thread(target=work1)
# t2 = Thread(target=work2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(f'线程创建后，g_num的值是{g_num}')

#列表

def work1(nums):
    nums.append(100)
    print("----in work1, nums is %s---" % nums)
def work2(nums):
    print("----in work2, nums is %s---" % nums)

nums = [1,2,3]
print(f'线程创建前，nums的值是{nums}')
t1 = Thread(target=work1,args=(nums,))
t2 = Thread(target=work2,args=(nums,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f'线程创建后，nums的值是{nums}')
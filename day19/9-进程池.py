# 作者: 学不会
# 2026年11月02日20时44分51秒
# xxx@qq.com
from multiprocessing.pool import Pool
import os, time, random


def worker(msg):
    start = time.time()
    print("%s 开始执行,进程号为%d" % (msg,os.getpid()))
    time.sleep(random.random())
    print(f'{msg}：执行完毕，耗时为 {time.time() - start}')


if __name__ == '__main__':
    pool = Pool(4)
    for i in range(10):
        # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
        # 每次循环将会用空闲出来的子进程去调用目标
        pool.apply_async(worker, args=(i,))
    pool.close()  # 关闭进程池，关闭后po不再接收新的请求
    # pool.terminate() # 终止po中所有子进程
    pool.join()  # 等待po中所有子进程执行完成，必须放在close语句之后

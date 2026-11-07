# 作者: 学不会
# 2026年11月03日19时00分25秒
# xxx@qq.com
from multiprocessing import Manager, Pool
import time, random
import os


def reader(q):
    print(f'reader启动{os.getpid()},父进程为{os.getppid()}')
    for i in range(q.qsize()):
        print(f'reader读取{q.get()}')



def writer(q):
    print(f'writer启动{os.getpid()},父进程为{os.getppid()}')
    for i in range(10):
        q.put(i)
        # time.sleep(1)
    # q.put(None)

if __name__ == '__main__':
    print(f'主进程启动{os.getpid()}')
    # 创建一个队列
    q = Manager().Queue()
    po=Pool()
    po.apply_async(writer, args=(q,))
    time.sleep(2)
    po.apply_async(reader, args=(q,))
    po.close()
    po.join()
    print(f'主进程结束{os.getpid()}')


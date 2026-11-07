# 作者: 学不会
# 2026年11月02日20时43分58秒
# xxx@qq.com
from multiprocessing import Process, Queue
import time, random


# 写数据进程执行的代码:
def write(q):
    for i in range(10):
        # print(i)
        q.put(i)
    q.put(None)


# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print(value)
            time.sleep(2)
        else:
            break


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    p1 = Process(target=write, args=(q,))
    p2 = Process(target=read, args=(q,))
    # 启动子进程p1，写入:
    p1.start()
    time.sleep(0.5)
    # 启动子进程p2，读取:
    p2.start()
    # 等待p1,p2结束:
    p1.join()
    p2.join()
    print('所有数据都写入并且读完')

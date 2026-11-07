# 作者: 学不会
# 2026年11月03日19时56分03秒
# xxx@qq.com
# 如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确

import threading

# 全局变量
counter = 0


def add1():
    global counter

    for i in range(100000):
        lock.acquire()  # 获取锁
        counter += 1
        lock.release()


def add2():
    global counter
    for i in range(100000):
        lock.acquire()
        counter += 1
        lock.release()


if __name__ == '__main__':
    # 创建锁
    lock = threading.Lock()
    # 创建线程
    t1 = threading.Thread(target=add1)
    t2 = threading.Thread(target=add2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(counter)

# 作者: 学不会
# 2026年11月03日19时24分18秒
# xxx@qq.com


import threading
import time, os

def print1():
    for i in range(3):
        print("----1----")
        time.sleep(1)
def print2():
    for i in range(3):
        print("----2----")
        time.sleep(1)

if __name__ == '__main__':
    print("----开始----")
    t1=threading.Thread(target=print1)
    t2=threading.Thread(target=print2)
    t1.start()
    t2.start()
    print(f'当前线程数量：{threading.active_count()}')
    t1.join()
    t2.join()


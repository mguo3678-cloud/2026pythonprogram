# 作者: 学不会
# 2026年10月31日15时28分50秒
# xxx@qq.com

from multiprocessing import Process
import time


def run():
    while True:
        print("----------1----------")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=run)
    p.start()
    while True:
        print("----------2----------")#1,2交替输出
        time.sleep(1)

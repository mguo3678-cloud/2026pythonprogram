# 作者: 学不会
# 2026年11月03日19时33分19秒
# xxx@qq.com
import threading
import time


class MyThread(threading.Thread):

    def run(self):
        for i in range(3):
            time.sleep(1)
            print(f'Thread {self.name} is running, i = {i}')


if __name__ == '__main__':
    t = MyThread()
    t.start()

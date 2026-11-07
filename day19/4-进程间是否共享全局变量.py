# 作者: 学不会
# 2026年11月02日20时42分59秒
# xxx@qq.com

from multiprocessing import Process

num=0

def work1():

    global num
    num=100
    print(f'num in work1: {num}')

if __name__ == '__main__':

    p1=Process(target=work1)
    p1.start()

    num=200
    p1.join()

    print(f'num in main: {num}')


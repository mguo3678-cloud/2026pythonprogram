# 作者: 学不会
# 2026年11月02日20时43分28秒
# xxx@qq.com

from multiprocessing import Process

my_list = [11, 22]


def work1(my_list):
    for i in range(3):
        my_list.append(i)
    print(f'子进程中的my_list：{my_list}')



if __name__ == '__main__':
    p = Process(target=work1, args=(my_list,))
    p.start()
    print(f'主进程中的my_list：{my_list}')
    p.join()
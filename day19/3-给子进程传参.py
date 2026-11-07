# 作者: 学不会
# 2026年11月02日20时42分36秒
# xxx@qq.com

from multiprocessing import Process

def run_proc(name,age,**kwargs):
    print(f'子进程 {name} 正在运行，年龄 {age}')
    print(kwargs)
    exit(5)


if __name__ == '__main__':
    p=Process(target=run_proc,args=('zhangsan',20),kwargs={'sex':'male','nation':'China'})
    p.start()
    print(p.is_alive())
    # p.terminate()
    p.join()
    print(f'子进程已经结束，退出码 {p.exitcode}')
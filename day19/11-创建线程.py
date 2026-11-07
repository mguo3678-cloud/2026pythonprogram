# 作者: 学不会
# 2026年11月03日19时20分32秒
# xxx@qq.com
import time
# 单线程
# def saySorry():
#     print("亲爱的，我错了，我能吃饭了吗？")
#     time.sleep(1)
# if __name__ == "__main__":
#     for i in range(5):
#         saySorry()

# 多线程
import threading


def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()  # 启动线程

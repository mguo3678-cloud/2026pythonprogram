# 作者: 学不会
# 2026年10月16日19时15分07秒
# xxx@qq.com

from collections import deque


# #增删查改
# queue = deque(["Eric", "John", "Michael"])
# queue.append('luke')
# print(queue)
# print(queue.popleft())
# print(queue)
# queue[0] ='xiongda'
# print(queue[0])

class deque1:
    def __init__(self):
        self.queue = []

    def empty(self):
        return len(self.queue) == 0

    # 入队
    def push_front(self, value):
        self.queue.insert(0, value)

    def push_rear(self, value):
        self.queue.append(value)

    # 出队
    def pop_front(self):
        if self.empty():
            return
        return self.queue.pop(0)

    def pop_rear(self):
        if self.empty():
            return
        return self.queue.pop()

    # 查看队头
    def front(self):
        if self.empty():
            return
        return self.queue[0]

    # 查看队尾
    def rear(self):
        if self.empty():
            return
        return self.queue[-1]

    # 查看队列长度
    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    d = deque1()
    d.push_front(1)
    d.push_front(2)
    d.push_rear(3)
    d.push_rear(4)
    print(d.queue)
    print('*'*50)
    print(d.front())
    d.pop_rear()
    d.pop_front()
    print(d.queue)
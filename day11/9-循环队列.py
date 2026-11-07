# 作者: 学不会
# 2026年10月16日19时15分22秒
# xxx@qq.com

class CircularQueue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = [0] * maxsize
        self.front = 0
        self.rear =0
    #入队
    def enqueue(self,ele):
        if (self.rear+1)%self.maxsize==self.front:
            print("队列已满")
            return
        self.queue[self.rear]=ele
        self.rear=(self.rear+1)%self.maxsize
    #出队 逻辑删除
    def dequeue(self):
        if self.front==self.rear:
            print("队列为空")
            return
        ele=self.queue[self.front]
        self.queue[self.front]=0  #逻辑删除
        self.front=(self.front+1)%self.maxsize
        return ele

if __name__ == '__main__':
    cq = CircularQueue(5)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.enqueue(6)
    print(cq.queue)
    ret=cq.dequeue()
    print(cq.queue)


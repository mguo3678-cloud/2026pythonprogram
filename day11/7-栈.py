# 作者: 学不会
# 2026年10月16日19时06分07秒
# xxx@qq.com

class Stack:
    def __init__(self):
        self.stack = []

    # 压栈
    def push(self, value):
        self.stack.append(value)

    # 出栈
    def pop(self):
        return self.stack.pop()

    # 查看栈顶元素
    def top(self):
        if self.empty():
            print("栈为空")
            return
        return self.stack[-1]

    # 查看栈的大小
    def size(self):
        return len(self.stack)

    # 判断栈是否为空
    def empty(self):
        return len(self.stack) == 0


if __name__ == '__main__':
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    print(s1.top())
    print(s1.size())
    print(s1.empty())
    print(s1.stack)

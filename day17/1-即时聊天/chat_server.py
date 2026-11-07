# 作者: 学不会
# 2026年10月29日19时47分55秒
# xxx@qq.com

import socket
import select
import sys


class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #端口复用
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(10)
        self.epoll = select.epoll()

    def chat_server(self):
        conn, addr = self.sock.accept()  # 等待客户端连接
        print("客户端连接成功", addr)
        self.epoll.register(conn.fileno(), select.EPOLLIN) # 注册客户端连接的文件描述符
        self.epoll.register(sys.stdin.fileno(), select.EPOLLIN) # 注册标准输入的文件描述符
        while True:
            events=self.epoll.poll(-1)#等待事件发生
            for fd,event in events:
                if fd==sys.stdin.fileno():#如果标准输入有数据
                    # 先读取标准输入
                    data = input()
                    # 然后发送给客户端
                    conn.send(data.encode('utf-8'))
                elif fd==conn.fileno():
                    # 最后读取客户端发送的数据
                    data = conn.recv(1024).decode('utf-8')
                    if data:
                        print(data)
                    else:
                        print("客户端断开连接")
                        return


if __name__ == '__main__':
    server = ChatServer('127.0.0.1', 8000)
    server.chat_server()

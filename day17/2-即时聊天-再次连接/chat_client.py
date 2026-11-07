# 作者: 学不会
# 2026年10月29日19时47分55秒
# xxx@qq.com

import socket
import select
import sys
#epoll 多路复用
class ChatClient:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.epoll = select.epoll()


    def chat_client(self):
        self.epoll.register(self.sock.fileno(), select.EPOLLIN)
        self.epoll.register(sys.stdin.fileno(), select.EPOLLIN)
        while True:
            #等待事件发生
            events = self.epoll.poll()
            for fd,event in events:
                if fd==self.sock.fileno():
                    #接收服务器发送数据
                    data = self.sock.recv(1024).decode('utf-8')
                    if not data:
                        return
                    print(data)

                elif fd==sys.stdin.fileno():
                    #读取标准输入
                    data=input()
                    #发送数据给服务器
                    self.sock.send(data.encode('utf-8'))



if __name__ == '__main__':
    host = '127.0.0.1'
    port=8000
    chat_client = ChatClient(host, port)
    chat_client.chat_client()


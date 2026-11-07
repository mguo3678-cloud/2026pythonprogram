# 作者: 学不会
# 2026年10月30日16时11分20秒
# xxx@qq.com
from socket import *

tcp_server_socket = socket(AF_INET, SOCK_STREAM)

# 重用对应地址和端口
tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 本地IP地址和端口
address = ('127.0.0.1', 8000)
tcp_server_socket.bind(address)
# 端口激活
tcp_server_socket.listen(100)
tcp_server_socket.setblocking(False)
client_socket = None
while True:
    try:
        client_socket, address = tcp_server_socket.accept()
        print('客户端地址：', address)
    except Exception as e:
        if client_socket:
            data = client_socket.recv(1024)
            if data:
               print(data.decode('utf-8'))
            else:
                print('客户端断开连接')
                break



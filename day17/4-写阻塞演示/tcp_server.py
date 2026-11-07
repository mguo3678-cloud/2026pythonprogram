# 作者: 学不会
# 2026年10月30日16时44分45秒
# xxx@qq.com

from socket import *

# 创建tcp_server_socket
tcp_server_socket = socket(AF_INET, SOCK_STREAM)

#重用对应的地址和端口
tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 绑定地址和端口
tcp_server_socket.bind(('127.0.0.1', 8080))

# 监听
tcp_server_socket.listen(100)

client_socket, address = tcp_server_socket.accept()

while True:
    pass


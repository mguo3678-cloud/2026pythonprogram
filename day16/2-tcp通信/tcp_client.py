# 作者: 学不会
# 2026年10月29日14时17分40秒
# xxx@qq.com

from socket import socket, AF_INET, SOCK_STREAM

# 创建socket对象
client_socket = socket(AF_INET, SOCK_STREAM)

# 连接服务器
client_socket.connect(('127.0.0.1', 8080))

# 发送数据
client_socket.send(b'Hello, Server!')

# 接收数据
data = client_socket.recv(1024)
print('Received:', data.decode())

# 关闭socket
client_socket.close()

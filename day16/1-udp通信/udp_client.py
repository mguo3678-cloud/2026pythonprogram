# 作者: 学不会
# 2026年10月29日10时25分51秒
# xxx@qq.com
import socket
from socket import AF_INET, SOCK_DGRAM

# 创建UDP套接字
udp_socket = socket.socket(AF_INET, SOCK_DGRAM)
server_add = ('127.0.0.1', 8080)
# 发送数据
udp_socket.sendto('Hello, Server!'.encode('utf-8'), server_add)
# 接收服务器的响应数据
recv_data, _= udp_socket.recvfrom(1024)
print("服务器响应:", recv_data.decode('utf-8'))

udp_socket.close()
# 作者: 学不会
# 2026年10月29日10时26分03秒
# xxx@qq.com

import socket

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建UDP套接字,使用ipv4协议
udp_server.bind(('127.0.0.1', 8080))  # 绑定服务器地址和端口
recv_data = udp_server.recvfrom(1024)  # 接收数据,最大接收1024字节
print(recv_data[0].decode('utf-8'))  # 打印接收到的数据
print(recv_data[1])  # 打印客户端地址和端口
udp_server.sendto(b'Hello Client', recv_data[1])  # 发送数据给客户端
udp_server.close()  # 关闭套接字

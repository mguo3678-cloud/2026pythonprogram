# 作者: 学不会
# 2026年10月30日17时20分17秒
# xxx@qq.com
"""
步骤
1.创建TCP套接字
建立网络通信工具
2.连接服务器
连接127.0.0.18080
3.接收文件名
知道服务器发送的是什么文件
4.接收文件大小
确定需要接收多少字节
5.循环接收文件内容
每次接收最多1024字节，写入文件
6.关闭文件和套接字
完成文件下载
"""

import struct                 # 导入 struct 模块，用于处理字节和整数之间的转换
from socket import *           # 导入 socket 模块中的所有内容，用于网络通信


# 创建 TCP 客户端套接字
tcp_client_socket = socket(AF_INET, SOCK_STREAM)
# AF_INET：表示使用 IPv4 地址
# SOCK_STREAM：表示使用 TCP 协议


# 设置服务器的 IP 地址和端口号
addr = ('127.0.0.1', 8080)
# 127.0.0.1：本机 IP 地址，也叫 localhost
# 8080：服务器使用的端口号


# 连接服务器
tcp_client_socket.connect(addr)
# 使用 connect() 方法连接指定的服务器


# 接收文件名
train_len = tcp_client_socket.recv(1024)
# 接收服务器发送的数据，最多接收 1024 个字节
# 这里接收到的是文件名长度信息


file_name = tcp_client_socket.recv(struct.unpack('I', train_len)[0])
# struct.unpack('I', train_len)：将字节数据转换成无符号整数
# [0]：取出转换后的整数
# recv()：根据文件名长度，接收完整的文件名


print(file_name)               # 打印接收到的文件名（二进制数据）


# 创建文件，准备接收文件内容
file = open(file_name.decode('utf-8'), 'wb')
# decode('utf-8)：将字节类型的文件名转换成字符串
# 'wb'：以二进制写入模式打开文件
# 如果文件不存在就创建，如果存在就覆盖原文件


# 接收文件内容的总长度
train_len = struct.unpack('I', tcp_client_socket.recv(4))[0]
# recv(4)：接收服务器发送的 4 个字节
# struct.unpack('I', ...)：将 4 个字节转换成无符号整数
# 得到整个文件的大小（字节数）


total = 0                     # 记录已经接收到的文件大小，初始为 0


# 循环接收文件内容，直到接收完毕
while total < train_len:

    text_bytes = tcp_client_socket.recv(1024)
    # 每次最多接收 1024 个字节的文件内容

    total += len(text_bytes)
    # 将本次接收到的字节数累加到 total 中
    # len(text_bytes)：计算本次接收到多少个字节

    file.write(text_bytes)
    # 将接收到的文件内容写入本地文件


file.close()                  # 关闭文件，释放文件资源

tcp_client_socket.close()     # 关闭 TCP 客户端套接字，断开连接
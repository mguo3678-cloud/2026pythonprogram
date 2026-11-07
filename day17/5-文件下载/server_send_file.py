# 作者: 学不会
# 2026年10月30日17时20分02秒
# xxx@qq.com
"""
服务器端
发送数据
发送文件名长度
发送文件名
发送文件大小
发送文件内容
"""
import os                       # 导入 os 模块，用于获取文件大小等操作
import struct                   # 导入 struct 模块，用于字节和整数之间的转换
from socket import *             # 导入 socket 模块中的所有内容，用于网络通信


# 创建 TCP 服务器套接字
tcp_server_socket = socket(AF_INET, SOCK_STREAM)
# AF_INET：表示使用 IPv4 地址
# SOCK_STREAM：表示使用 TCP 协议


# 设置地址重用
tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# SOL_SOCKET：表示设置套接字选项
# SO_REUSEADDR：允许服务器地址和端口重复使用
# 1：表示开启这个功能，方便服务器重新启动


# 绑定地址
tcp_server_socket.bind(('127.0.0.1', 8080))
# 127.0.0.1：本机 IP 地址
# 8080：服务器端口号
# bind()：将 IP 地址和端口号绑定到服务器套接字


# 监听客户端连接
tcp_server_socket.listen(5)
# listen(5)：开始监听客户端连接
# 5：表示等待连接队列的最大长度


# 接收客户端连接
client_socket, client_address = tcp_server_socket.accept()
# accept()：等待客户端连接
# client_socket：与客户端通信的新套接字
# client_address：客户端的 IP 地址和端口号


file_name = 'text.txt'           # 设置要发送给客户端的文件名


# 防止粘包：先发送文件名
# 获取文件名的长度
train_len_bytes = struct.pack('I', len(file_name.encode('utf-8')))
# file_name.encode('utf-8')：将文件名转换成字节类型
# len()：计算文件名占用的字节数
# struct.pack('I', ...)：将整数打包成 4 字节的无符号整数
# train_len_bytes：保存打包后的文件名长度


# 发送文件名长度
client_socket.send(train_len_bytes)
# 将文件名长度发送给客户端


# 把文件名放到火车车厢发过去
client_socket.send(file_name.encode('utf-8'))
# 将文件名转换成字节类型后发送给客户端


# 获取文件长度
file_size = os.path.getsize(file_name)
# os.path.getsize()：获取文件大小，单位是字节


# 将文件大小打包成 4 字节数据
train_len_bytes = struct.pack('I', file_size)
# 将文件大小转换成无符号整数对应的 4 字节数据


# 发送文件大小
client_socket.send(train_len_bytes)
# 告诉客户端整个文件有多少字节


# 打开文件
file = open(file_name, 'rb')
# 'rb'：以二进制只读模式打开文件
# 适合发送图片、视频、文档等各种类型的文件


# 发送文件内容
while True:
    data = file.read(1024)
    # 每次从文件中读取 1024 个字节

    if not data:
        break
    # 如果读取不到数据，说明文件已经读取完毕
    # break：结束循环

    client_socket.send(data)
    # 将读取到的文件内容发送给客户端


file.close()                     # 关闭文件，释放文件资源

client_socket.close()            # 关闭与客户端通信的套接字

tcp_server_socket.close()        # 关闭服务器套接字

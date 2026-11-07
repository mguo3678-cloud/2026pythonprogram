# 作者: 学不会
# 2026年10月30日16时45分12秒
# xxx@qq.com
from socket import *

# 创建套接字
tcp_client_socket = socket(AF_INET, SOCK_STREAM)

# 本地IP地址和端口号

addr = ('127.0.0.1', 8080)

# 连接服务器
tcp_client_socket.connect(addr)

data = 'hello,world' * 1000
total = 0
# 循环发送数据
while True:
    try:
        # 发送数据
        send_size = tcp_client_socket.send(data.encode('utf-8'))
        total += send_size
        print('发送了%d字节数据' % send_size)
    except Exception as e:
        print(f"{e}")
        break

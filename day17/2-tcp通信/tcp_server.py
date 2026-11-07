# 作者: 学不会
# 2026年10月29日14时17分54秒
# xxx@qq.com

from socket import socket, AF_INET, SOCK_STREAM

# 创建socket对象
tcp_server=socket(AF_INET, SOCK_STREAM)

# 绑定地址和端口
tcp_server.bind(('127.0.0.1', 8080))

# 监听客户端连接,5表示最多同时监听5个客户端连接
tcp_server.listen(5)

# 接收客户端连接,#3次握手发生在这里
client_socket, client_addr = tcp_server.accept()
print('客户端地址：',client_addr)

# 接收客户端发送的数据
data = client_socket.recv(5)
print('客户端发送的数据：',data.decode('utf-8'))
# 发送数据给客户端
client_socket.send('你好，客户端！'.encode('utf-8'))

#关闭客户端连接
client_socket.close()
#关闭服务器
tcp_server.close()

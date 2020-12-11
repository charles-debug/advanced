import socket

# 创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# 绑定端口号
tcp_server_socket.bind(("", 8000))

# 设置监听
tcp_server_socket.listen(128)

# 等待接受连接
# 循环等待链接，服务多个客户端
while True:
    new_socket, ip_port = tcp_server_socket.accept()
    print(ip_port)
    # 接受请求数据
    recv_data = new_socket.recv(4096)
    print(recv_data)

    with open("D:/APPS/Microsoft VS Code/new_works/static/index.html","rb") as f:
        file_data = f.read()
    # 把要发送的信息封装为http格式
    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 响应头
    response_head = "Server: PWS1.0\r\n"
    # 空行

    # 响应体
    response_body = file_data

    response_data = (response_line + response_head + "\r\n").encode('utf-8') + response_body
    # 把字符串编码成二进制
    
    send_data = new_socket.send(response_data)

    # 关闭服务于客户端的套接字
    new_socket.close()

    




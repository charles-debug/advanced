import socket


# 1.建立套接字
# AF_INET:IPV4
# SOCK_STREAM: TCP传输协议

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.和套接字建立连接
tcp_client_socket.connect(("127.0.0.1",9090))
# 3.发送数据
send_content = "你好，我是客户端小白！！！"  # 也可以使用input
# 对字符串编码成二进制
send_data = send_content.encode("utf-8")
# windows里面的网络调试助手使用的是GBK格式
# linux 和mac OS使用的是utf—8
tcp_client_socket.send(send_data)
# 4. 接受数据
recv_data = tcp_client_socket.recv(1024)
recv_content = recv_data.decode("utf-8")
print(recv_content )

# 5.关闭套接字
tcp_client_socket.close()
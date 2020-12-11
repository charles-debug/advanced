import socket
import threading

def handle_client_request(ip_port, new_client):
    print("接受客户端端口号为：", ip_port)
    # 5. 接受请求
    while True:
        recv_data = new_client.recv(1024)
        if recv_data:
            print("接受的数据长度为：", len(recv_data))
            recv_content =recv_data.decode("utf-8")
            print("接受客户端数据为：", recv_content)

            # 6. 发送数据
            send_content = "问题正在处理中....."
            send_data = send_content.encode("utf-8")
            new_client.send(send_data)
        else:
            print("客户端下线了...", ip_port)
            break
    # 关闭服务与客户端的套接字，表示和客户端终止通信
    new_client.close()

if __name__ == "__main__":
    # 1. 创建套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口号复用：服务端程序退出端口号立即释放
    # 参数1：当前套接字
    # 参数2：端口号复用选项
    # 参数3：选项对应的值
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, True)
    # 2. 绑定端口号
    # 第一个参数不用指定，表示使用本机ip即可
    # 第二个参数表示端口号
    tcp_server_socket.bind(("", 8080))
    # 3. 设置监听
    # 128表示最大建立连接数
    tcp_server_socket.listen(128)
    # 4. 等待客户端连接请求
    # 注意点：每次客户端和服务端建立连接时都会返回新的套接字
    # tcp_server_socket只负责接受客户端的连接请求，收发消息不使用该套接字
    while True:
        new_client, ip_port = tcp_server_socket.accept()
        # 代码执行到此，说明客户端和服务端建立连接成功
        sub_thread = threading.Thread(target=handle_client_request, args=(ip_port, new_client))
        sub_thread.start()
        

    # 7. 关闭套接字
    tcp_server_socket.close()

    # 关闭服务端套接字表示，服务端不再等待接受任何客户端的连接请求

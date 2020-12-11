import socket
import threading
import sys

class HttpWebServer(object):
    def __init__(self, port):
            
        # 创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        # 绑定端口号
        tcp_server_socket.bind(("", port))

        # 设置监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket  = tcp_server_socket

    # 等待接受连接
    @staticmethod
    def handle_client_request(new_socket):
        # 接受请求数据
            recv_data = new_socket.recv(4096)
            # print(recv_data)
            if len(recv_data) == 0:
                print("关闭浏览器了")
                new_socket.close()
                return
            # print(recv_data)
            recv_content = recv_data.decode("utf-8")
            request_list = recv_content.split(" ", maxsplit=2)
            request_path = request_list[1]
            print(request_path)

            if request_path == "/":
                request_path = "index.html"
            # 判断是否存在
            # os.path.exists
            # 异常
            try:

                with open("D:/APPS/Microsoft VS Code/new_works/static/" + request_path,"rb") as f:
                    file_data = f.read()

            except Exception as e:
                with open('D:/APPS/Microsoft VS Code/new_works/static/error.html', 'rb') as f:
                    file_data = f.read()

                # 响应行
                response_line = "HTTP/1.1 404 Not Found\r\n"
                # 响应头
                response_head = "Server: PWS1.0\r\n"
                # 空行

                # 响应体
                response_body = file_data
                response_data = (response_line + response_head + "\r\n").encode('utf-8') + response_body
                # 把字符串编码成二进制
                
                new_socket.send(response_data)

            else:
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
                
                new_socket.send(response_data)
            finally:
                # 关闭服务于客户端的套接字
                new_socket.close()

    def start(self):
        # 循环等待链接，服务多个客户端
        while True:
            new_socket, ip_port = self.tcp_server_socket.accept()
            print(ip_port)

            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request, args= (new_socket,))
            # 设置成为守护主线程
            sub_thread.setDaemon = True
            # 启动子线程
            sub_thread.start()


def main():
    params = sys.argv
    if len(params) != 2:
        print("命令格式如下：python xxxx.py 9000")
        return

    if not params[1].isdigit():
        print("命令格式如下：python xxxx.py 9000")
        return
    port = int(params[1])
    webserver = HttpWebServer(port)
    webserver.start()

if __name__ == "__main__":
    main()

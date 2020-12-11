import threading
import time

# 定义全局变量
g_list = []

def add_data():
    for i in range(3):
        g_list.append(i)
        print("read", i)
        time.sleep(0.3)
    print("list:", g_list)
def read_data():
    print("data", g_list)


if __name__ == "__main__":
    add_thread = threading.Thread(target = add_data)
    read_thread = threading.Thread(target = read_data)

    add_thread.start()
    # time.sleep(1)
    # 主线程等待子线程执行结束以后，再往下执行任务
    add_thread.join()
    read_thread.start()


import threading

import time

def task():
    time.sleep(1)
    # 获取当前线程
    print(threading.current_thread())


if __name__ == "__main__":
    # 循环创建大量线程，测试线程之间执行是否是无序的
    for i in range(20):
        # 每循环一次创建一个子线程
        sub_thread = threading.Thread(target=task)

        sub_thread.start()

        # 线程之间的执行是无序的，具体哪个线程执行是由CPU决定的
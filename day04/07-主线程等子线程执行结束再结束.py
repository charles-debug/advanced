import threading
import time


def task():
    while True:
        print("任务执行中......")
        time.sleep(0.3)
if __name__ == "__main__":
# daemon = true 表示创建的子线程守护主线程，主线程退出子线程直接销毁
    # sub_thread = threading.Thread(target = task)
    # sub_thread = threading.Thread(target = task, daemon=True)
    sub_thread = threading.Thread(target = task)
    sub_thread.setDaemon(True)
    sub_thread.start()


    # 主线程延迟一秒执行
    time.sleep(1)
    print("over")

    # 结论： 主线程会等待所有子线程执行结束再结束

    # 解决办法： 设置子线程为守护主线程
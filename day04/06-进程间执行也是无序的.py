import multiprocessing

import time

def task():
    time.sleep(1)
    # 获取当前进程
    print(multiprocessing.current_process())


if __name__ == "__main__":
    # 循环创建大量进程，测试进程之间执行是否是无序的
    for i in range(20):
        # 每循环一次创建一个子线程
        sub_process = multiprocessing.Process(target=task)

        sub_process.start()

        # 进程之间的执行是无序的，具体哪个线程执行是由CPU决定的
import threading

# 定义全局变量
g_num = 0
# 任务1 循环100万次每次加1
def task1():
    # 这是一个不可变类型，一旦发生更改内存地址也会发生改变，因此需声明全局变量
    global g_num
    for i in range(1000000):
        g_num += 1

    print("first num:", g_num)

def task2():
    # 这是一个不可变类型，一旦发生更改内存地址也会发生改变，因此需声明全局变量
    global g_num
    for i in range(1000000):
        g_num += 1

    print("second num:", g_num)

# 创建子线程
if __name__ == "__main__":
    first_thread = threading.Thread(target = task1)
    second_thread = threading.Thread(target=task2)

    first_thread.start()
    # 解决方法1 
    first_thread.join() # 线程等待 
    # 让主线程等子线程1执行完之后，再继续后面的操作
    second_thread.start()

# 两个线程可能同时调用同一个全局变量，在一个为完成加数之前，就调用了全局变量，导致数值小于200万
# 解决方法： 1. 线程等待   2. 互斥锁
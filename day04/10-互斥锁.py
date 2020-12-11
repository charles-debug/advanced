import threading

# 定义全局变量
g_num = 0

# 创建互斥锁，这个锁本质上是一个函数
lock = threading.Lock()
# 任务1 循环100万次每次加1
def task1():
    # 这是一个不可变类型，一旦发生更改内存地址也会发生改变，因此需声明全局变量
    lock.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1

    print("first num:", g_num)

    lock.release()

def task2():
    # 这是一个不可变类型，一旦发生更改内存地址也会发生改变，因此需声明全局变量
    lock.acquire()
    global g_num
    for i in range(1000000):
        g_num += 1

    print("second num:", g_num)

    lock.release()

# 创建子线程
if __name__ == "__main__":
    first_thread = threading.Thread(target = task1)
    second_thread = threading.Thread(target=task2)

    first_thread.start()
    # 解决方法1 
    first_thread.join() # 线程等待 
    # 让主线程等子线程1执行完之后，再继续后面的操作
    second_thread.start()

# 线程等待和互斥锁都是保证同一时刻只有一个任务执行，能保证全局变量的数据没问题
# 线程等待和互斥锁都是把多任务改成单任务去执行，保证了数据准确性，但执行性能会下降
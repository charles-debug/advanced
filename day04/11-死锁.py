# 根据下标在列表中取值, 保证同一时刻只能有一个线程去取值
import threading

#创建互斥锁
lock = threading.Lock()

def get_value(index):
    lock.acquire()
    
    my_list = [1, 4, 6]
    if index >= len(my_list): 
        print("下标越界：", index)
        # 当下标越界需要释放锁，让后面的线程还可以取值
        lock.release()
        # return 后面的代码将不能执行，故而下面的这个所一直不能释放，就会出现死锁
        return

    value = my_list[index]
    print(value)
    lock.release()


# 创建线程
if __name__ == "__main__":
    for i in range(10):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()
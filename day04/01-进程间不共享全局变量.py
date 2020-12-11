import multiprocessing
import time


# 因为列表是可变类型，可在原有的基础上修改数据，并且修改后内存地址不变
# 所以不需要加上global关键字
# 加上global表示声明要修改全局变量的地址
g_list = list()

#创建添加数据的方法
def add_data():
    for i in range(3):
        g_list.append(i)
        print("add:", i)

        time.sleep(0.2)
    print(g_list)

# 创建读取方法
def read_data():
    print("data:", g_list)


if __name__ == '__main__':
    add_process = multiprocessing.Process(target= add_data)
    read_process = multiprocessing.Process(target=read_data)


    add_process.start()
    add_process.join()
    read_process.start()

# 结论  进程间不共享全局变量

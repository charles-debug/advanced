# #1 导入进程包
# import multiprocessing
# import time
# #创建跳舞任务
# def dance():
#     for i in range(3):
#         print("跳舞中......")
#         time.sleep(0.5)
# #创建唱歌任务
# def sing():
#     for i in range(3):
#         print("唱歌中......")
#         time.sleep(0.5)
# if __name__ == "__main__":
# #2 创建子进程(自己创建的进程称为子进程)
#     dance_process = multiprocessing.Process(target = dance)


# #3 启动进程执行响应的任务
#     # dance_process.start()
#     sing()


#1 导入进程包
import multiprocessing
import time
#创建跳舞任务
def dance():
    for i in range(3):
        print("跳舞中......")
        time.sleep(0.5)
#创建唱歌任务
def sing():
    for i in range(3):
        print("唱歌中......")
        time.sleep(0.5)
if __name__ == "__main__":
#2 创建子进程(自己创建的进程称为子进程)
    dance_process = multiprocessing.Process(target = dance)
    sing_process = multiprocessing.Process(target = sing)

#3 启动进程执行响应的任务
    dance_process.start()
    sing_process.start()


# 进程的执行的无序的，看CPU安排
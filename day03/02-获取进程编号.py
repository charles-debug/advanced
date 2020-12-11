#1 导入进程包
import multiprocessing
import time
import os
#创建跳舞任务
def dance():
    # 获取当前进程编号（主进程）
    dance_process_id = os.getpid()
    #获取当前进程对象，查看进程是有哪个代码执行的：multiprocessing.current_process
    print("dance_process_id:", dance_process_id, multiprocessing.current_process())
    dance_process_parent_id = os.getppid()
    print("dance_process的父进程编号是：", dance_process_parent_id)

    for i in range(3):
        print("跳舞中......")
        time.sleep(0.5)
        os.kill(dance_process_id, 9)
#创建唱歌任务
def sing():
    # 获取当前进程编号（主进程）
    sing_process_id = os.getpid()
    #获取当前进程对象，查看进程是有哪个代码执行的：multiprocessing.current_process
    print("sing_process_id:", sing_process_id, multiprocessing.current_process())
    sing_process_parent_id = os.getppid()
    print("sing_process的父进程编号是：", sing_process_parent_id)
    for i in range(3):
        print("唱歌中......")
        time.sleep(0.5)
        
# 获取当前进程编号（主进程）
main_process_id = os.getpid()
#获取当前进程对象，查看进程是有哪个代码执行的：multiprocessing.current_process
print("main_process_id:", main_process_id, multiprocessing.current_process())

if __name__ == "__main__":
#2 创建子进程(自己创建的进程称为子进程)
    dance_process = multiprocessing.Process(target = dance, name = "dance_process")
    print("dance_process:", dance_process)
    sing_process = multiprocessing.Process(target = sing, name = "sing_process")
    print("sing_process:", sing_process)

#3 启动进程执行响应的任务
    dance_process.start()
    sing_process.start()
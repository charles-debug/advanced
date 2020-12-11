import threading
import time

# 定义唱歌方法
def sing():
    current_thread = threading.current_thread()
    print("sing：", current_thread)


    for i  in range(3):
        print("唱歌中.....")
        time.sleep(0.2)

def dance():
    current_thread = threading.current_thread()
    print("sing：", current_thread)
    
    
    for i in range(3):
        current_thread = threading.current_thread
        
        print("跳舞中.......")
        time.sleep(0.2)

# 创建入口模块
if __name__ == "__main__":
    current_thread = threading.current_thread()
    print("main_thread:", current_thread)
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    # 启动线程

    sing_thread.start()
    dance_thread.start()

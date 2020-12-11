# 导入包
import multiprocessing

#定义任务
def show_info(name,age):
    print(name,age)
if __name__ == '__main__':

    # # 创建进程
    # sub_process = multiprocessing.Process(target = show_info, args = ("李四", 20))
    # # 以元组方式传参，元组里的元素顺序和参数里的顺序一致

    # #启动任务
    # sub_process.start()

    # 创建进程
    sub_process = multiprocessing.Process(target = show_info, kwargs = {"age" : 20, "name":"王五"})
    # 以元组方式传参，元组里的元素顺序和参数里的顺序一致

    #启动任务
    sub_process.start()
import threading

# 创建函数
def show_info(name,age):
    print("name: %s age: %d"%(name,age))

# 创建子线程

if __name__ == "__main__":

    # 以元组的方式传参必须保证元组里面元素的顺序与函数里面元素的顺序一致

    # sub_thread = threading.Thread(target=show_info, args=("李四", 20))
    # sub_thread.start()
    
    # 以字典的形式传参，必须保证字典的key值与函数的参数名保持一致
    sub_thread = threading.Thread(target=show_info, kwargs={"name":"李四","age":20})
    sub_thread.start()
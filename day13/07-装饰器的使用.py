import time

# 定义装饰器
def decorator(func):
    def inner():
        # 执行函数开始的时间
        begin = time.time()  # ————time.time()出现的时间是距离1970-1-1-0-0-1秒的时间
        func() # 执行work()函数
        # 执行结束额时间
        end = time.time()
        result = end - begin
        print(result)
    return inner

@decorator   # 装饰器就等价于work = decorator(work)
def  work():
    for i in range(100):
        print(i)

work()
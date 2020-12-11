# ------带有参数和返回值的函数---------
# 添加装饰器
def decorator(func):
    def inner(a,b):
        print("正在执行加法")
        num = func(a,b)
        return num
    return inner

@decorator
def add_num(num1,num2):
    result = num1 + num2
    # print(result)
    return result

result = add_num(1,2)    
print("结果为:",result)



# ------带有不定长参数和返回值的函数----------
def decorator(func):
    # 使用装饰器装饰已有函数时，内部函数要和已有函数的类型一致
    def inner(*args,**kwargs):
        print("正在执行加法")
        # 这里对不定长参数进行拆包，仅限于结合不定长参数使用
        num = func(*args,**kwargs)
        return num
    return inner

@decorator
def add_num(*args,**kwargs):
    result = 0
    # * args元组类型
    # **args是字典类型
    for value in args:
        result += value

    for value in kwargs.values():
        result += value
    # print(result)
    return result

result = add_num(1,2)    
print("结果为:",result)


#来个装饰器
def make_div(func):
    print("div 装饰器开始..........")
    def inner():
        result = "<div>" + func( )+ "</div>"
        
        return result
    return inner
def make_p(func):
    print("p 装饰器开始..........")
    def inner():
        result = "<p>" + func( )+ "</p>"
        
        return result
    return inner

@make_div
@make_p
def moto():
    return "人生苦短，我用python"

result = moto()
print(result)
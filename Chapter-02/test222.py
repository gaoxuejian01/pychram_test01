"""
装饰器函数带参数
"""

def out_f(arg):
    print("out_f="+arg)
    def decorator(func):
        def inner():
            func()
            print("inner的函数")
        return inner
    return decorator

@out_f("123")

def func():
    print("fnuc函数")

if __name__ == "__main__":
    func()
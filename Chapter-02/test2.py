"""
装饰器  ：增加功能
实质： 是一个函数
参数：被装饰函数名
返回：返回一个函数
作用：为已经存在的对象添加额外的功能
"""


def demo(func):    #装饰器函数 是一个带参数and 下面必须有一个函数
    def inner():
        func()
        print('装饰器inner函数的打印')
    return inner

@demo#装饰器出现在哪个函数的上面就是将下面的函数当做参数  传给 @后面的函数的参数

def target():
    print("打印一个target的函数")

if __name__ == "__main__":
    target()
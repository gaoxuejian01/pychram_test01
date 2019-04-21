"""
装饰器联系
"""


import time

def decorator(func ):
    def wrapper():
        start_time =time.time()
        func()
        end_time = time.time()
        print(start_time,end_time,end_time-start_time)
    return wrapper

@decorator

def func():
    print("hello world")
    time.sleep(1)

if __name__ == "__main__":
    func()
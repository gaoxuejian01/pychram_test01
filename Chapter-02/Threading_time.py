import threading
import time

def helloworld():
    time.sleep(2)#等待了2秒   所有倒是 main hello world 再出现helleworld
    print('helleworld')

t=threading.Thread(target=helloworld)  #Thread函数调用helloworld
t.start()#这个start才是开始target  后面的函数的开始
# helloworld()
print('main  helloworld')
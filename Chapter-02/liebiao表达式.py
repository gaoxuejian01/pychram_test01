"""
列表表达式
"""
#
#
# l = [1,2,3,4,5]
# l2=[item+1 for item in l]
# print(l2)


# l3=[item**2 for item in l]
# print(l3)

#
# l4 = [item for item in l if item <3]
# # print(l4)
#
#
# # l = (x**2 for x in  range(10))#这是生成os器表达式
#
# # print(l.__next__())
# # print(l.__next__())
# # print(l.__next__())
# # print(l.__next__())
#
#
import os
# #返回当前目录
os.getcwd()
# #列出目录的内容
# os.listdir()
# #创建目录
# os.mkdir("te")
# #删除空目录
# os.rmdir("te")
# #重命名
# os.rename('1.py','2.py')
# #删除文件
# os.remove('2.py')
# #执行系统命令
# os.system("ls")
# #退出程序
# os._exit(0)
print(os.getcwd())
# g=os.walk('/Users/gaoxuejian/')
# print(type(g))
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

import os.path

# os.path.abspath()

# print(os.path.abspath())
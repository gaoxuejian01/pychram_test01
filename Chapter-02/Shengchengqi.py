"""
生成器是一种用函数语法定义的迭代器; 调用生成器函数返回一个迭代器
yield语句挂起生成器函数并向调用者发送一个值，迭代器的_next__继续运行函数
"""

# l = [[1, 2], [3, 4], [5, ]]
# def flat(l):
#     for sublist in l:
#         for e in sublist:
#             yield e   #yied相当于返回一值，不结束的  return
# #
#
# def gen():
#     for i in range(10):
#         x = (yield i)
#         print("x=",x)




def gen():
    for i in range(10):
        yield i

g1=gen()
g2=gen()

print(next(g1))#g1 执行循环一次暂停
print(next(g2))#g2 执行循环一次暂停
print(next(g1))#g1 执行循环一次暂停
print(next(g2))#g2 执行循环一次暂停
print(next(g1))#g1 执行循环一次暂停
print(next(g2))#g2 执行循环一次暂停





# if __name__ == "__main__":
#     g = gen()
#     next(g)  #没有打印 所有从1开始  如果打印后就是从0开始了
#     print("g.send(11)",g.send(11))
#     print("g.send(22)",g.send(22))

    # L=flat(l)
    # # print(next(L))
    # for num in L:
    #     print(num)


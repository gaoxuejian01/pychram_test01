"""
生成器是一种用函数语法定义的迭代器; 调用生成器函数返回一个迭代器
yield语句挂起生成器函数并向调用者发送一个值，迭代器的_next__继续运行函数
"""

l = [[1, 2], [3, 4], [5, ]]
def flat(l):
    for sublist in l:
        for e in sublist:
            yield e   #yied相当于返回一值，不结束的  return




if __name__ == "__main__":

    L=flat(l)
    # print(next(L))
    for num in L:
        print(num)
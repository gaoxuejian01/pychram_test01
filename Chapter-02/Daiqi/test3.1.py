"""
迭代的意思是重复做一些事很多次，for循环就是一种迭代，列表，字典，元组都是可迭代对象
实现__iter__方法的对象都是可迭代的对象。 iter 返回一个迭代器，
所谓迭代器就是具有next方法的对象 在掉用next方法的时，
迭代器会返回它的下一个值，如果没有值了，则返回StopIteration
"""

#斐波那契数
class Fibs:
    def __init__(self):
        self.a=0
        self.b=1

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self


if __name__ == "__main__":
    fibs = Fibs()

    for f in fibs:
        if f<1000:
            print(f)
        else:
            break



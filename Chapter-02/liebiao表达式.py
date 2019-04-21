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
# print(l4)


l = (x**2 for x in  range(10))

print(l.__next__())
print(l.__next__())
print(l.__next__())
print(l.__next__())
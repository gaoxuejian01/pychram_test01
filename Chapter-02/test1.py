


"""
取出嵌套列表内的所有元素
"""


def get_list(l):
    for i in l:
        if isinstance(i,list):
            get_list(i)
        else:
            print(i)
if __name__ == "__main__":
    l = [1,2,[4,5],3]
    get_list(l)
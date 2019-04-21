"""
abspath() 将相对路径转化为绝对路径 os.path.abspath(path)
dirname() 获取完整路径当中的目录部分 os.path.dirname("d:/1/test")
basename()获取完整路径当中的主体部分 os.path.basename("d:/1/test")
split() 将一个完整的路径切割成目录部分和主体部分 os.path.split("d:/1/test")
join() 将2个路径合并成一个 os.path.join("d:/1", "test")
getsize() 获取文件的大小 os.path.getsize(path)
isfile() 检测是否是文件 os.path.isfile(path)
isdir() 检测是否是文件夹 os.path.isdir(path)
"""

import os.path

print(os.path.abspath('os_patch'))
print(os.path.dirname("/Users/gaoxuejian/PycharmProjects/pychram_test01/Chapter-02/os_patch"))
print(os.path.basename('/Users/gaoxuejian/PycharmProjects/pychram_test01/Chapter-02'))
print(os.path.split('/Users/gaoxuejian/PycharmProjects/pychram_test01/Chapter-02/os_patch'))
print(os.path.join('/Users/gaoxuejian/PycharmProjects/pychram_test01/Chapter-02/Daiqi','test2'))
print(os.path.getsize('/Users/gaoxuejian/'))
print(os.path.isfile('/Users/gaoxuejian/'))
print(os.path.isdir("/Use rs/gaoxuejian/"))
"""
递归函数列出所有文件 使用os.listdir os.isfile
练习找出单个目录中的最大文件
练习找出目录树中的最大文件
"""

import os

def files_digui_dir(pathdir):
    for i in os.listdir(pathdir) :
        filepatch=os.path.join(pathdir,i)
        if os.path.isdir(filepatch):
           files_digui_dir(filepatch)
        else:
            print(filepatch)
if __name__ =="__main__":

    files_digui_dir('/Users/gaoxuejian/')


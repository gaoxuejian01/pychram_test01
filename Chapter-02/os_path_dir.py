import os

for dirpath,dienames,filenames in  os.walk('/Users/gaoxuejian/PycharmProjects/pychram_test01/Chapter-02/'):
    print('['+dirpath+']')
    for filename in filenames:
        print(os.path.join(dirpath+filename))
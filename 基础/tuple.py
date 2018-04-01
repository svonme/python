# -*- coding: utf-8 -*-
#
# @Time    : 2018/3/28 14:13
# @Author  : svon.me@gmail.com
#

# tuple : 元组，是一种有序的列表，和list非常类似，但是tuple一旦初始化就不能修改

if __name__ == '__main__':

    # 初始化一个元组对象
    names = ('张三', '李四', '王五', '赵六')

    print(names)

    for index, value in enumerate(names):
        print('下标 : %d, 内容 : %s' % (index, value))
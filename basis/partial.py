# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/12 09:38
# @Author  : svon.me@gmail.com
#

# 偏函数, 创建默认参数的函数

import functools

# 定义一个默认转换8进制的函数, 底层实现为系统int 函数
int8 = functools.partial(int, base=8)


if __name__ == '__main__':
    '''
        int8("8") = int("8", base=8)
    
    '''

    value = "101111"

    print("8进制 %s = %d" % (value, int8(value)))
# -*- coding: utf-8 -*-
#
# @Time    : 2018/4/9 10:32
# @Author  : svon.me@gmail.com
#

# 装饰器

import time

def log(func):
    def wrapper(*args, **kw):

        time_start = time.time()  # 函数运行开始时间

        # 接收多返回值, python 的返回值是一个 tuple(元组) 类型，这里用 （）包含，定义 result 为 tuple 类型
        result = (func(*args, **kw))

        time_stop = time.time()  # 函数运行结束时间
        print('%s函数运行时间花费了%d秒:' % (func.__name__, time_stop - time_start))
        # 返回结果
        return result

    return wrapper


@log
def test(*args):
    sum = 0  # 定义求和变量
    for i in args:
        sum += i
    return sum

# print(test(*list(range(10))))
print(test(1, 2, 3, 4, 5, 6, 7))

# 设置一个路由
def router(path):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (path, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@router("/index")
def app():
    print("router - index")

app()

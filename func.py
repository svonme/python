# -*- coding: utf-8 -*-
#
# @Time    : 2018/3/30 16:50
# @Author  : svon.me@gmail.com
#


# 返回一个数的绝对值
def _abs(value):
    num = int(value)
    if num > 0:
        return num
    return num * -1


# 定义参数默认值
def power(num, n=2):
    sum = num
    for i in range(n - 1):
        sum *= float(num)
    return sum


def info(name=None, age=25, sex="F", city="北京"):
    print("姓名: %s" % name)
    print("性别: %s" % sex)
    print("年龄: %s" % age)
    print("地区: %s\n" % city)


# 可变参数
def calc(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum


if __name__ == '__main__':
    number = -1
    print('number = %d, number 的绝对值为 %s\n' % (number, _abs(number)))

    num = 5
    print('%d 的平方等于 %d * %d = %d\n' % (num, num, num, power(num, 2)))

    # 指定参数名称传值
    info('张三', 20, city="上海")

    print('calc 1 + 2 + 3 = %d\n' % calc(1, 2, 3))

    print('扩展list calc(*[1, 2, 3]) = %d\n' % calc(*[1, 2, 3]))

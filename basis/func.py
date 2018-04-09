# -*- coding: utf-8 -*-
#
# @Time    : 2018/3/30 16:50
# @Author  : svon.me@gmail.com
#


# 返回一个数的绝对值
def _abs(value):
    # 判断数值类型
    if not isinstance(value, (int, float)):
        raise TypeError('bad operand type')

    if value > 0:
        return value
    return value * -1


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

# 多返回值
# python 返回值是一个tuple。在语法上，返回一个tuple可以省略括号，
# 而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以 Python 的函数返回多值其实就是返回一个tuple
def person():
    name = "张三"
    age = 25
    sex = "男"
    return name, age, sex

# 可变参数
def calc(*numbers):
    count = 0
    for n in numbers:
        count = count + n
    return count


if __name__ == '__main__':
    number = -1
    print('number = %d, number 的绝对值为 %s\n' % (number, _abs(number)))

    num = 5
    print('%d 的平方等于 %d * %d = %d\n' % (num, num, num, power(num, 2)))

    # 指定参数名称传值
    info('张三', 20, city="上海")

    print('calc 1 + 2 + 3 = %d\n' % calc(1, 2, 3))

    print('扩展list calc(*[1, 2, 3]) = %d\n' % calc(*[1, 2, 3]))

    print('多返回值: 姓名=%s, 年龄=%s, 性别=%s\n' % person())

    _num = (1, 2, 3, 4, 5, 6, 7)
    print('可变参数: calc%s = %d\n' % (_num, calc(*_num)))

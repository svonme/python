# -*- coding: utf-8 -*-
#
# @Time    : 2018/3/29 17:00
# @Author  : svon.me@gmail.com
#

if __name__ == '__main__':

    num1 = 10
    num2 = 5

    if num1 > num2:
        print('num1 > num2')
    pass

    if num2 < num2:
        print('num1 > num2')
    else:
        print('num2 < num1')
    pass

    name = "张三"

    if name:
        print("name = %s" % name)
    pass

    sex = None

    if not sex:
        print('当 sex 为空时 条件为真')
    pass

    age = 20

    if name and age >= 20:
        print('name = %s, age = %d' % (name, age))
    pass

    arr = list(range(100 + 1))
    count = 0

    for i in arr:
        count += arr[i]

    print('for 循环计算 1 - 100 之间的自然数和为 %d' % count)

    i = 100
    count2 = 0

    while i > 0:
        count2 += i
        i -= 1
    pass

    print('while 循环计算 1 - 100 之间整数的和为 %d' % count2)

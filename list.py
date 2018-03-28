# -*- coding: utf-8 -*-
#
# @Time    : 2018/3/28 11:50
# @Author  : svon.me@gmail.com
#

# list是一种有序的集合，可以随时添加和删除其中的元素

if __name__ == '__main__':
    arr = ['张三', '李四', '王五']
    item = arr[1]  # 获取某一个元素
    print('数组 ', arr)
    print('某个元素 : %s', item)

    # 在末尾追加一个元素
    arr.append('赵六')

    # 指定位置添加元素
    # 把元素添加到索引为 2 的位置，以前的元素从索引为 2 开始，全部向后移动
    arr.insert(2, '小明')

    print('修改后的数组 : ', arr)

    last = arr.pop()  # 删除最后一个元素并把这个元素的值返回
    print('最后一个元素的内容为 %s' % last)
    print('删除后的数组内容 : ', arr)

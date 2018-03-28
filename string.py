# -*- coding: utf-8 -*-




if __name__ == '__main__':

    str = 'Hello, %s, 我是%s' % ('world', '字符串')

    encode = str.encode()

    print('encode编码 %s' % encode)

    print('decode解码 %s ' % encode.decode('utf-8'))

    print('ASCII A = %s' % ord('A'))
    print('ASCII 65 = %s' % chr(65))

    text = '计算字符串长度使用 len 方法'

    print('text = "%s", 字符的长度为 %d' % (text, len(text)))

# -*- coding: utf-8 -*-
"""
    7.12.py
    ~~~~~~~

        访问定义在闭包内的变量
"""
# 一般来说，闭包内层定义的变量是不可被外界访问的，但是我们可以对闭包中的变量应用
# 存取函数，并将存取函数作为属性附加到闭包上，这样就可以对闭包内的变量进行访问。
def close_func():
    n = 0 # 闭包内部定义的变量
    def func():
        print ('n=', n)

    # 编写存取函数
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # 把存取函数作为闭包的属性
    func.get_n = get_n
    func.set_n = set_n
    return func

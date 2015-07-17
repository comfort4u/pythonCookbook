# -*- coding: utf-8 -*-

"""
    7.3.py
    ~~~~~~

        将元数据信息附加到函数参数上
"""
# 这是python3的新特性－－参数注解
# : 后的注解信息都不会被编译
# 注解只会存储在 __annotations__ 属性中
# 但是增加注解后函数签名就会多出类型表示
# 其实python是动态语言，是没必要指定类型的
# 注解只是方便程序员阅读源代码
def add(x:int, y:int) -> int:
    return x + y
    

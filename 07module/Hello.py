#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module ' # 模块的文档注释
__author__ = 'Michael Liao'

# 以上是python 标准
# 模块的文档注释 任何模块代码的第一个字符串都被视为模块的文档注释；

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':  # __name__指向 _main_
    test()

print(sys.argv)

# python 作用域
# 定义私有变量
# Python并没有一种方法可以完全限制访问private函数或变量
def __private_1(name):
    return 'Hello,%s' %name
def __private_2(name):
    return 'Hi,%s' %name
def greeting(name):
    if len(name) > 3:
        return  __private_1(name)
    else:
        return  __private_2(name)
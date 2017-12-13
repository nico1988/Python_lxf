# -*- coding: utf-8 -*-

#高阶函数  js里边叫回调函数
print(abs(10))
print(abs(-19))
f = abs
print(f(19))
# abs = 10
# print(abs(10)) #报错


# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x,y,f):
    return f(x)+f(y)
print(add(-1,-2,abs))

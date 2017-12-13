# -*- coding:utf-8 -*-
# 迭代器
# 可迭代对象 list tuple dict set str
# generator generator function
from collections import Iterable
# 用isinstance()判断一个对象是否是Iterable对象：
print(isinstance([],Iterable))
print(isinstance('a',Iterable))
print(isinstance([x for x in range(10)],Iterable))
print(isinstance(199,Iterable))
# 用isinstance()判断一个对象是否是Iterable对象：
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance('a',Iterator))
print(isinstance(1,Iterator))
print(isinstance({'a':"b"},Iterator))
print(isinstance(iter([]),Iterator))
print(isinstance(iter('a'),Iterator))
print(isinstance(iter({'a':1}),Iterator))
# Iterator 对象可以被next函数调用


#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；


# 理解python for 循环
it = iter([1,2,3,4,5])
# 循环
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
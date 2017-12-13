# -*- coding:utf-8 -*-
# iteration 迭代
# python 的 迭代通过 for in 完成
# for in 可以迭代 list tuple dict

# 判断是否可以迭代

L = list(range(100))
from collections import Iterable
print(isinstance('a',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance((1,2),Iterable))
print(isinstance(123,Iterable)) # 整数不能迭代
print(L)
for i,v in enumerate(L):
    print(i,v)

# 循环两个变量
for x,y in [(1,1),(2,3),(3,9)]:
    print(x,y)

# 寻找最小值和最大值
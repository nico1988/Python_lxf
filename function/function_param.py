# -*- coding:utf-8 -*-
import os
import math

# python 函数的参数十分灵活
# 位置参数--必选参数
# 默认参数
# 可变参数
# 关键字参数
# 命名参数
# 可变参数+命名参数
# 命名参数+默认参数

# 位置参数
def power(x):
    return  x * x
print(power(9))
def power_f(x):
    return math.sqrt(x)
print(power_f(9))
# 默认参数
def power(x,n=2):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s
print(power(10,2))
print(power(10))

# 默认参数的坑
# l 是一个变量
# 总结：默认参数一定要是一个变量
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end([1,2,3]))
print(add_end([1,2,3]))
print(add_end())
print(add_end())


# 可变参数  注意星号
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return  sum
nums = [1,2,3,4]
print(calc(1,2,3,4))
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print(calc(*nums))  # 已有list或者touple调用可变参数在签名加*

# 关键字参数
# 用连个** 定义
# 用处  ： 扩展函数的功能，比如注册的非必填项目
def person(name,age,**kw):
    print('name:', name, "age:",age,"other:",kw)
person('nico',29,city="beijing")
# 这样调用报错 person('nico',29,'beijing')
# python 会把后面的当成位置参数
extra = {'city':'beijing','job':'Engineer'}
person('ruirui',29,job=extra['job'])
person('tiantian',1,**extra)

# 命名关键字参数
# 限制调用者传入 限制  的关键字参数
def x_person(name,age,*,city,job):
    print(name,age,city,job)
x_person('nico',29,city='长沙',job='Engneer')

# 可变参数+ 命名关键字参数
def mm_person(name,age,*args,city,job):
    print(name,age,args,city,job)
mm_person('nico',29,city='changsha',job='engneer')
mm_person('nico',29,1,2,3,city='changsha',job='engneer')
mm_person('nico',29,*nums,city='changsha',job='engneer')


# 可变参数+ 默认参数
def mr_person(name,age,*,city="changsha",job):
    print(name,age,city,job)
mr_person('nico',29,job='engneer')

# 参数组合
def f1(a,b,c=0,*args,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a,b,c=0,*,d,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)
f1(1,2,4)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x='00')
f2(1,2,d='d',ext=None)

# 传入 dict 和 touple
args = (1,2,3,4)
kw = {'d':99,'e':100}
f1(*args,**kw)
args = (1,2,3)
f2(*args,**kw)
# -*- coding:utf-8 -*-
def my_abs(x):
    if x>0:
        return x
    else:
        return -x
print(my_abs(-19))

print('定义空函数 占位置')
def kong():
    pass
if True:
    pass
# 参数错误
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad type; please check out")
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-19))

# 返回多个值 其实就是一个touple
import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x,y = move(100,100,60,math.pi/6)
r = move(100,100,60,math.pi/6)
print(x,y)
print(r)

# 定义一个一元二次方程函数
print('**********一元二次方程求解**********')
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError("a is not a number")
    if not isinstance(b,(int,float)):
        raise TypeError("b is not a number")
    if not isinstance(c,(int,float)):
        raise TypeError("c is not a number")
    d=b*b-4*a*c
    if a==0:
        if b==0:
            if c==0:
                return '方程根为全体实数'
            else:
                return '方程无根'
        else:
            x1=-c/b
            x2=x1
            return x1,x2
    else:
        if d<0:
            return '方程无根'
        else:
            x1 = (-b + math.sqrt(d))/2/a
            x2 = (-b - math.sqrt(d))/2/a
            return x1,x2
# print(quadratic(1,-1,"a"))
print(quadratic(1,2,0))
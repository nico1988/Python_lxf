# Partial 偏函数
# 简化参数书写  调用时更简单

print(int('12211',base=8))
print(int('12345',base=16))

# 定义一个函数
def int2(x,base=2):
    return int(x,base)
print(int2('10'))


# Partial python提供的偏函数
import functools
int2 = functools.partial(int,base=2)
int3 = functools.partial(int,base=10)
# patrial 相当于把函数的参数固定住
print(int2('1111'))
print(int3('100000'))

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，

int3 = functools.partial(max,10,20)
print(int3(1,2,3))
print(int3(1,2,30))
args = [1,2,3]
kw = {"base":2}
int4 = functools.partial(int,*args)
print(int4('10'))
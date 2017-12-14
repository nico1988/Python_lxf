# 高阶参数
# map
# 参数
# 函数
# Iterable
def f(x):
    return x*x
r = map(f,range(10))
print(list(r))
print(list(map(str,range(19))))
print(list(map(abs,[1,2,-1])))


# reduce
from functools import reduce
def add(x,y):
    return x+y
red = reduce(add,[1,2,3,4,5])
print(red)

def to_int(x,y):
    return x*10 + y
print(reduce(to_int,[1,2,3,4,5]))


# 实现字符串转整数
def to_str(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(to_int,map(to_str,'13579')))

# 实现首字母大写
def normalize(name):
    return "%s" % (name[:1].upper() + name[1:]) # %s字符串替换
print(normalize('abc'))
print(list(map(normalize,['ABC','abc'])))
print("abc%s" % 'def')

# 利用reduce求积
def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn,L)

print(prod([1,2,3,4]))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
def str2float(s):
   def fn(x, y):
        return x * 10 + y
   def char2num(s):
        digist = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digist[s]
   # 先map 处理字符串list [1, 2, 3, 4, 5, 6, 7]
   # 再reduce 将list处理成整数
   return reduce(fn, map(char2num, s.replace(".","")))
s="1234.567"
if s.find("."): # 这里逻辑有问题  s.find('.')找不到为 -1
     print('str2float(\'%s\') ='%s, str2float(s)/pow(10,(len(s)-s.find(".")-1))) # pow 返回x的y次方
else:
     print('str2float(\'%s\') ='%s, str2float(s))
def char2num(s):
    digist = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digist[s]
print(list(map(char2num,s.replace('.',''))))


# 字符串转数字
def str_to_float(str):
    def fn(x,y):
        return x * 10 + y
    def char_to_num(item): # 这里的item是str的每一个字符
        digist = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digist[item]
    if ('.' in str): # 这里不能用 str.find('.')做判断
        # 先map 处理字符串list [1, 2, 3, 4, 5, 6, 7]
        # 再reduce 将list处理成整数  1234567
        # pow 返回10的指数
        return reduce(fn,map(char_to_num,str.replace('.','')))/pow(10,len(str)-str.find('.')-1)
    else:
        return reduce(fn,map(char_to_num,str))
str = '123.4567'
str0 = '12'
print('str=',str_to_float(str))
print('str0=',str_to_float(str0))
print(str_to_float('123.434'))
print(str_to_float('12332323.434'))
print('1213'.find("3"))

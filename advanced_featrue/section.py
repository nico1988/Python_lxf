# 切片
# 去list或者tuple的一部分
L = [1,2,3,4,5]
# 最笨的方式
print([L[0],L[1]])
# 循环
r = []
n = 3
for i in range(n):
    r.append(i)
print(r)
# for i in range(n)
print(list(range(5)))
print(range(10)[2])
# list 切片
L = list(range(100))
print(L[0:3])
print(L[0:2])
print(L[:2])
print(L[1:2])
print(L[-10:])
print(L[10:20])
print(L[:10:3])
print(L[::4])
print(L[:])
# tuple切片
T = tuple(range(100)) # 生成1-100的元组
print(T)
print(T[:3])
# 字符串切片
str = 'abcdefg'
print(str[3:5])
print(str[3])
# 利用切片实现trim方法
# print(str[])

print(' dsfd '.strip())
print('ad'.strip('a'))
print('nico'.strip('n'))

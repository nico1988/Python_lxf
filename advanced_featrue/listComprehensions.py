# 列表生成式
print(list(range(1,10)))
L = []
for x in range(1,11):
    L.append(x*x)
print(L)

# 列表生成式可以替代循环
LC = [x*x*x for x in range(1,11)]
print(LC)
print([m+n for m in 'ABC' for n in 'XYZ'])


# 一条语句显示本地的文件
import os
print([d for d in os.listdir('.')])
print([d for d in os.listdir("C:/")])
print([d for d in os.listdir("D:/")])
print([d for d in os.listdir('e:/')])

# 循环dict
d = {'x':'a','y':'b','z':'c'}
for k,v in d.items():
    print(k,'=',v)
print([k + '=' + v for k,v in d.items()])

# 把一个list全部变小
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
print(isinstance('abc',str))
print(isinstance(1,str))
print(isinstance(1,int))
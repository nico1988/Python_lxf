# -*- coding:utf-8 -*-
# 排序算法
print(sorted([1,24,2,3,2,3323,4,232]))

# 定义key进行排序
print(sorted([1,3,-12,33,-1223,-32],key=abs))

# 字符串排序 默认按照ascii码排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 忽略大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
# 反向排序
print(sorted(['abc','efd','Adsf','BDCD'],key=str.lower,reverse=True))

# 对一组tuple进行排序

# 这里不是太懂，过后再说
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L))
print(sorted(L,reverse=True))
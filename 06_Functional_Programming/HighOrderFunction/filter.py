# Python内建的filter()函数用于过滤序列。
# 去掉奇数只保留
def is_odd(n):
    return n%2 == 1
print(list(filter(is_odd,[1,2,3,4,5,6,7])))

# 去掉字符串序列中的空额和none
def not_empty(n):
    return n and n.strip()
print(list(filter(not_empty,["1",'','a',None])))

# 筛选素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

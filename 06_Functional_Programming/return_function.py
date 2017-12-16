# 将函数作为结果返回

# 参数求和
def calc_sum(*args):
    print(args)
    ax = 0
    for n in args: # args 是一个tuple
        ax = ax + n
    return ax
print(calc_sum(1,2,3))

# 返回函数  函数里边套函数 其实就是闭包

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
print(lazy_sum(1,2,4)())  # 注意这里有函数调用

f1 = lazy_sum(1,2,3,4)
f2 = lazy_sum(1,2,3,4)
print(f1 == f2) #False


# 闭包
print(list(range(1,4)))
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count() # 调用时i已经是3了
print(f1()) # 9
print(f2()) # 9
print(f3()) # 9

#  返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count_1():
    fs = []
    def f(j):
        def g():
            return j*j
        return g
    for i in range(1,4):
        fs.append(f(i))
    return fs
f4,f5,f6 = count_1()
print(f4()) # 9
print(f5()) # 9
print(f6()) # 9


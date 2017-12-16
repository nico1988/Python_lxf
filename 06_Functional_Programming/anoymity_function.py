# 匿名函数

# lambda表达式
# 相当于定义了一个函数  返回改函数参数表达式
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
lam = lambda x: x*x
print(lam(8))
print((lambda x: x*x)(8))

# 将匿名函数当做返回值返回
def build(x,y):
    return lambda b: x*x + y*y + b
print(build(2,4)(2))


def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)

lam_is_odd = lambda n: n%2 == 1
lam_L = list(filter(lam_is_odd, range(1, 20)))  # filter函数会自动调用lam_is_odd，将参数传进去
print(lam_L)
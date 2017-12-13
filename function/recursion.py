# 递归 recursion
def recursion0(n):
    if n==1:
        return 1
    return n * recursion0(n-1)
print(recursion0(100))
# print(recursion0(1000))  # RecursionError: maximum recursion depth exceeded in comparison
# 解决堆栈溢出  尾递归
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact_iter(4,1))
print(fact_iter(59,1))
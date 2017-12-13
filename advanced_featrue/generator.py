# generator
# generator 保存的是算法 不是值  list保存的是值
# 每次调用next(g) 太麻烦一般不用
g = (x*x for x in range(10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
for x in g:
    print(x)

# 斐波那契数列
# 前两项的和是第三项 除第一个外
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n +1
    return 'done'
print(fib(10))

# 利用generator 算出
def gen_fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield(b)
        a,b = b,a+b
        n = n + 1
    return 'done'
gen_f = gen_fib(10)
print(next(gen_f))
print(next(gen_f))

def odd():
    print('step 1')
    yield 1
    print('s 2')
    yield 2
    print('s3')
    yield 3
o = odd()
print(next(o))
print(next(o))
print(next(o))

# 拿到generator 的返回值
while True:
    try:
        x = next(gen_f)
        print('gen_f',x)
    except StopIteration as e:
        print('generator retrun value:',e.value)
        break

print('杨辉三角 ')
def triangles(line):
    L = [1]
    n =1
    while n<line:
        yield L  # 保存list
        L=[L[x] + L[x+1] for x in range(len(L)-1)]   # list生成器 打印list中间的值
        L.insert(0,1) #开始加1
        L.append(1) # 最后加1
        n = n +1;
tri = triangles(10)
for item in tri:
    print(item)

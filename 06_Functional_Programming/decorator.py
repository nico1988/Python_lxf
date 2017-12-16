# 装饰器 Decorator
# 增强函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# _name_
def name():
    print('name')
print(name.__name__)  # __name__ 获取函数的名字

def now():
    print('2017-12-15')
f = now
f()
print(f.__name__)

# 定义一个打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__,'end') # 打印日志
        return func(*args, **kw) # 执行原始的now函数
    return wrapper
@log  # 相当于执行了log函数  now = log(now)
# now指向了新的变量  执行now() 相当于执行了 wrapper() 函数
def now():
    print('2015-3-25')
now()

import functools,time

def log(text):
    def decorator(func):
        @functools.wraps(func)  # 解决__name__
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')  # now = log('execute')(now)
def now():
    print('2015-3-25')
print(now.__name__) # wrapper

def metric(fn):
    print('%s executed in %s ms' % (fn.__name__,10.24))
    return fn
@ metric #fast = metric(fast)
def fast(x,y):
    time.sleep(0.0012)
    return x + y;
now()

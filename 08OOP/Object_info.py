# 获取对象信息

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
class a(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
nico = a('nico',29)
print(type(nico))

# 判断是否函数   types模块
import types
def fn():
    pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)
print(isinstance('a',str))
print(isinstance(1,int))
print(isinstance(1,(list,tuple)))
print(isinstance([2],(list,tuple)))
print(dir(abs))
print('abc'.__len__())

# 模拟len
class MyDog(object):
    def __len__(self):
        return 1000
dog = MyDog()
print(dog.__len__())

print('abc'.lower())

#
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj,"x"))
print(hasattr(obj,'power'))
print(hasattr(obj,'y'))
print('设置属性')
setattr(obj,'x',99)
print('获取属性')
print(obj.x)
print(getattr(obj,'x',404)) # 这个应该用处很大
print(getattr(obj,'y',404))

def readImage(fp):
    if hasattr(fp,'read'):
        return  readData(fp)
    return None

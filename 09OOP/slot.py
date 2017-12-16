# 限制实例的属性   __slot__
class Student(object):
    __slots__ = ('name','age')
    # 用tuple定义允许绑定的属性名称
    # __slots__支队儿子管用，对孙子不管用
s = Student()
s.name = 'nico'
s.age = 29
print(s.name)
print(s.age)
print(Student.__name__)
class graduateStudent(Student):
    pass
g = graduateStudent()
g.score = 100
print(g.score)
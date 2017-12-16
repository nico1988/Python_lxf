# 定义类  和java一样
# 类和实例  class instance
# 类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
class Student(object):  # 没有extend关键字
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name,self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'a'
        elif self.score >=60:
            return 'b'
        else:
            return 'c'
nico = Student('nico',100)
# nico1 = Student()

print(nico)
print(nico.name)
print(nico.score)
print(nico.print_score())
print(nico.get_grade())

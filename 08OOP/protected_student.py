# 访问限制
# 私有变量 以两个_开头
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' %(self.__name,self.__score))
    def get__name(self):
        return self.__name
    def get__score(self):
        return self.print_score
    def set__name(self,name):
        self.__name = name
    def set__score(self,score):
        if 0<= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
nico = Student('nico00',100)
nico.set__score(99)
nico.print_score()
# 访问private 变量
print(nico._Student__name)
# python 中的特殊变量 __xx__ 可以直接访问
nico.__name = 'nico0000'
print(nico.get__name())
print(nico.__name)

# 练习

class Student00(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self,gender):
        return  self.__gender
    def set_gender(self,gender):
        if gender == 'male':
            self.__gender = gender
        else:
            print('bad gender')
ruirui = Student00('ruirui','female')
ruirui.set_gender('aa')
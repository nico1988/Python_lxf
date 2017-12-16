# 继承有什么好处？最大的好处是子类获得了父类的全部功能
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('dog ir running')

class Cat(Animal):
    def run(self):
        print('cat ir running')
dog = Dog()
# dog.run()

cat = Cat()
# cat.run()


# 理解多态
# 多态： 子类继承父类  子类的实例既是子类又是父类
def run_twice(animal):
    animal.run()
    animal.run()

print(run_twice(Animal()))
print(run_twice(Cat()))
print(run_twice(Dog()))



'''
1==True
0==False
print(True+False)
print(True-False)
print(True*False)
print(True/False)

class MyClass:
    """一个简单的类实例"""
    i=12345
    def f(self):
        return "Hello world!"


#实例化类
x = MyClass()

#访问类的属性和方法
print("Myclass 类的属性i为：",x.i)
print(x)
print("Myclass 类的方法f输出为：",x.f())
#print(MyClass.f(x))
print("\n")
class C:
    def get_self(self):
        print(self)
c=C()
print(c)
print(c.get_self())
print(C.get_self(c))


class C:
    def set_x(self,v):
            self.x=v  ##也即  c.x=v

c=C()
c.set_x(250)
print(c.__dict__)
print(c.x)
'''
#封装
class Student(object):

    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):      #直接在类的定义内部访问数据的函数即把数据“封装”起来
        print('%s:%s'%(self.name,self.score))
    def get_grade(self):        #增加新的方法
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'
bart = Student('Bart Simpson', 59)
#def print_score(std):          #外部访问
    #print('%s:%s'%(std.name,std.score))
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())

#继承
class Animal(object):
    def run(self):
        print('Animal is running...')

#当我们需要编写Dog和Cat类时，就可以直接从Animal类继承
class Dog(Animal):      #对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

#第一个好处：子类获得了父亲的全部功能
dog=Dog()
dog.run()

cat=Cat()
cat.run()
#第二个好处：多态
#当子类和父类存在相同的run()时，我没说，子类run()覆盖了父类run(),在代码运行时总是会调用子类的run()
def run_twice(animal):
    animal.run()
run_twice(Animal())             #传入Animal实例
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):         #新增子类不必对函数做任何修改
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())
# Python3推导式

## 列表推导式  

### 1. 基本格式  

> 【表达式 for变量 in列表】【out_exp_res for out_exp in input_list】
>
> 或者【表达式 for变量 if条件】【out_exp_res for out_exp in input_list if condition】
>
> 注：
>
> ```
> #out_exp_res：列表生成元素表达式，可以是有返回值的函数
> #for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中
> #if condition：条件语句，可以过滤列表中不符合条件的值
> ```

### 2. 实例  

- 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母

  ```
  names = ['Bob','Tom','alice','Jerry','Wendy']
  new_names = [name.upper()for name in names if len(name)>3]
  print(new_names)
  ```

- 计算 30 以内可以被 3 整除的整数

  ```
  multiples=[i for i in range(30) if i%3==0]
  print(multiples)
  ```

## 字典推导式    

### 1. 基本格式    

> { key_expr:value_expr for value in collection}   
>
> 或 { key_expr: value_expr for value in collection if condition }

### 2. 实例  

- 使用字符串及其长度创建字典  

  ```
  listdemo = ['Google','Runoob','Taobao']
  #将列表中个字符串值为键，各字符串的长度为值，组成键值对
  newdict = {key:len(key)for key in listdemo}
  print(newdict)
  ```

- 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典	

  ```
  dict={x:x**2 for x in (2,4,6)}
  print(dict)
  print(type(dict))
  ```

## 集合推导式  

### 1.基本格式  

> { expression for item in Sequence }
>
> 或者{ expression for item in Sequence if conditional }		

### 2.实例  

- 算数字 1,2,3 的平方数

  ```
  setnew={i**2 for i in (1,2,3)}
  print(setnew)
  ```

- 判断不是 abc 的字母并输出

  ```
  a={x for x in 'abracadabra' if x not in 'abc'}
  print(a)
  print(type(a))
  ```

## 元组推导式  

### 1.基本格式  

> (expression for item in Sequence )
>
> 或者（expression for item in Sequence if conditional )

### 2.实例  

- 使用下面的代码生成一个包含数字 1~9 的元组

  ```
  a=(x for x in range(1,10))
  print(a)      #<generator object <genexpr> at 00x000001C37ADF8890> # 返回的是生成器对象
  print(tuple(a))                            #使用tuple()函数，可以直接将生成器对象转化为元组
  ```

# Python3注释

- 单行注释以 # 开头  

- 多行注释用三个单引号''' 或者三个双引号""" 将注释括起来  

- 注：多行注释可以嵌套使用，但是单行注释不能嵌套使用  



# Python3条件控制  

### 1.if语句  

- 一般形式

  ```
  ```if condition_1:    statement_block_1 ```
  
  ```elif condition_2:    statement_block_2 ```
  
  ```else:    statement_block_3```  
  ```

  

- 注：1. 每个条件后要使用冒号，表示接下来是满足条件后要执行的语句块

​               2.使用缩进来划分无惧快，相同缩进数的语句在一起组成一个语句块

### 2.实例  

- 简单的if实例

  ```
  vary1 = 100
  if vary1:
      print("1-if表达之条件为true")
      print(vary1)
  
  vary2 = 0
  if vary2:
      print("2-if 表达式条件为true")
      print(vary2)			#由于变量Vary2为0，所以对应的if语句将不执行
  print("Good bye!")
  ```

- 狗的年龄计算判断

  ```
  age = int(input("请输入你家狗狗的年龄："))
  print("")
  if age <=0:
      print("你是子啊逗我吧！")
  elif age ==1:
      print("相当于14岁的人。")
  elif age ==2:
      print("相当于22岁的人。")
  else:
      human = 22 + (age-2)*5
      print("对应人类年龄：",human)
  ```

- 数字猜谜游戏

  ```
  number=7
  guess=-1
  print("数字猜谜游戏！")
  while guess !=number:
      guess =int(input("请输入你猜的数字："))
      
      if guess==number:
          print("恭喜，你猜对了！")
      elif guess < number: 
          print("猜的数字小了...")
      elif guess > number:
          print("猜的数字大了...")
  ```

### 3.if嵌套  

- 格式

  ```
  if 表达式1:
      语句
      if 表达式2:
          语句
      elif 表达式3:
          语句
      else:
          语句
  elif 表达式4:
      语句
  else:
      语句
  ```

- 简单实例

  ```
  num=int(input("输入一个数字：")) 
  if num%2==0:        
  	if num%3==0:               
  		print ("你输入的数字可以整除 2 和 3")        
  	else:        
  		print ("你输入的数字可以整除 2，但不能整除 3")
  else:   
  	if num%3==0:                
  		print ("你输入的数字可以整除 3，但不能整除 2")       
  	else:                
  		print  ("你输入的数字不能整除 2 和 3")`
  ```

### 4.match...case  

- 格式：

  ```:
  match subject:
  	case <pattern_1>:
  		<action-1>
  	case <pattern_2>:
  		<action_2>
  	case <pattern_3>:
  		<action_3>
  	case _:							#类似于default
  		<action_wildcard>
  #match后的对象依次与case后的内容进行匹配，如果匹配成功，则执行匹配到的表达式，否则直接跳过，_可以匹配一切
  ```

- 实例：输出HTTP状态码？

# Python3 循环语句  

### 1.while循环  

- 一般形式：

  ```
   while 判断条件(condition):`
  	`执行语句(statements)....`
  ```

- 实例：计算1到100的总和：

  ```
  n=100
  
  sum=0
  counter=1
  while counter <=n:
      sum+=counter
      counter+=1
  
  print("1 到 %d 之和为： %d" % (n,sum))
  ```

### 2.无限循环  

- 通过设置条件永远不为false来实现无限循环

- 实验你CTRL+C来退出当前的无限循环

- 无限循环在服务器上客户端的shishi请求非常有用

- 实例

  ```
  var=1
  while var==1:
      num =int(input("请输入一个数字："))
      print("你输入的数字是：",num)
  ```

### 3.while 循环使用else语句  

- 语法格式

  ```
  while <expr>:				#expr条件语句为true则执行statement(s)语句块
  	<statement(s)>			#如果为false，则执行additional_statement(s)
  else:
  	<additional_statement(s)>
  ```

- 实例：循环输出数字，并判断大小

  ```
  count = 0
  while count < 5:
      print(count,"小于5")
      count=count+1
  else:
      print(count,"大于或等于5")
  ```

### 4.简单语句组  

- 类似于if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中

### 5.for语句  

- 一般格式

  ```
  for <variable> in <sequence>:
  	<statements>
  else:
  	<statements>
  ```

- 实例：打印字符串中的每个字符

  ```
  word='run'
  for letter in word :
      print(letter)
  ```

### 6.for...else  

- 语法格式

  ```
  for item in iterable:  						#遍历iterable中的所有元素
  	#循环主体						         #执行else子句中的代码  
  else：									   #若遇break,则中断，不执行else
  	#循环结束后执行的代码
  ```

- 实例

  ```
  sites = ["Baidu","Google","Runoob","Taobao"]
  for site in sites:
      if site=="Runoob":
          print("cainiao")
          break
      print("循环数据"+site)
  else:
      print("没有循环数据！")
  print("完成循环！")
  ```

### 7.break和continue语句及循环中的else子句

- break语句可以跳出佛如和while的循环体。若在循环中终止则，任何对应的循环else将不执行

- continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续下一轮循环

- 实例：break

  ```
  var = 10
  while var > 0:
      print('当前变量值为：',var)
      var = var -1
      if var==5:
          break
  ```

- 实例：continue

  ```
  n=5
  while n>0:
      n-=1
      if n==2:
          continue
      print(n)
  print('循环结束')
  ```

- 循环语句可以有else子句，它在穷尽列表或条件变为false导致循环终止时被执行，弹循环被break终止时不执行

- 实例：查询质数

  ```
  for n in range(2,10):
      for x in range(2,n):
          if n % x == 0:
              print(n,'等于',x,'*',n//x)
              break
      else:
          #循环中没有找到元素
          print(n,'是质数')
  ```

### 8.pass语句

- 为空语句，不做任何事情，一般用做占位语句，是为了保持程序结构的完整性

  ```
  for letter in 'Runoob':
      if letter=='o':
          pass
          print('执行pass块')
      print('当前字母:',letter)
  ```

# Python3面向对象(一种代码封装的方法)

### 1.类（class）定义  

- 语法格式：

  ```statement
  class ClassName:				#class即自定义的对象数据类型
  								#ClassName即类名，用大写字母开头
  	<statement-1>
  	.
  	.
  	.
  	<statement-N>
  ```

### 2.类对象 (对象=属性+方法）

- 对象的方法即调用对象对应的关联函数，和普通函数不同，方法可以直接访问实例的数据

- 通过在实例上调用方法，就直接操作了对象内部的数据，但无需指定方法内部的实现细节

- 和静态语言不同，Python允许对实例变量绑定任何数据。也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

  

- 类对象支持两种操作：属性引用和实例化

  ```
  class MyClass:
      """一个简单的类实例"""
      i=12345
      def f(self):
          return 'hello world'
  
  #类MyClass实例化一个对象x
  x = MyClass()		#创建一个新的类实例并将该对象赋给局部变量x，x为空的对象
  
  #访问类的属性和方法
  print("Myclass 类的属性i为：",x.i)#调用
  print("Myclass 类的方法f输出为：",x.f())
  ```

- 由于类可以起到模板的作用，由此，可以在创建实例的时候，把一些我们人物为必须绑定的属性强制填写进去。通过一个特殊的\__init__方法：

  ```
  class Student(object):
  	
  	def __init__(self,name,score):
  		self.name=name
  		self.score=score
  ```

- \__init__方法的第一个参数永远是self, 指向类的实例化对象本身

  - 作用：绑定
  - 有了`__init__`方法，在创建实例的时候，就不能传入空的参数了，必须传入与`__init__`方法匹配的参数，但self不需要传，Python解释器自己会把实例变量串进去

  ```
  class C:
      def set_x(self,v):
              self.x=v  ##也即  c.x=v
  
  c=C()
  c.set_x(250)
  print(c.__dict__)
  print(c.x)
  ```

- 给实例对象添加属性

  - 点号+属性名称

###3.封装

- ```
  class Student(object):
  
      def __init__(self,name,score):
          self.name=name
          self.score=score     
     #直接在类的定义内部访问数据的函数即把数据“封装”起来
      def print_score(self): 
          print('%s:%s'%(self.name,self.score))
      def get_grade(self):        #增加新的方法（好处）
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
  ```

### 3.继承与多态  

- 第一个好处：子类获得了父亲的全部功能
- 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可被看作是父类。但是，反过来就不行

- 当子类和父类存在相同的run()时，我没说，子类run()覆盖了父类run(),在代码运行时总是会调用子类的run()
- 第二个好处：多态
  - 真正的威力：调用方只管调用，不管细节

- “开闭”原则

  - 对扩展开放：允许新增子类
  - 对修改封闭：不需要修改依赖Animal类型的run_twice等函数

  ```
    class Animal(object):
        def run(self):
            print('Animal in running...')
  #当我们需要编写Dog和Cat类时，就可以直接从Animal类继承
  #对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类
    class Dog(Animal):      
        def run(self):
            print('Dog is running...')
  
    class Cat(Animal):
        def run(self):
            print('Cat is running...')
    dog=Dog()
    dog.run()
  
    cat=Cat()
    cat.run()
  
    def run_twice(animal):
        animal.run()
    run_twice(Animal())             #传入Animal实例
    run_twice(Dog())
    run_twice(Cat())
  
    class Tortoise(Animal):         #新增子类不必对函数做任何修改
        def run(self):
            print('Tortoise is running slowly...')
  
    run_twice(Tortoise())
  ```
# Python数字类型（补充）  

### bool  （真假）

- 结果为false的所有情况
  - 定义为false的对象：None和false
  - 值为0的数字类型：0，0.0，0j(复数)，Decimal（0），Fraction（0，1）(分子为零，分母为1的有理数)
  - 空的序列和集合：'',(),[],{},set(),range()

- 布尔类型其实是特殊的整数类型，即bool是int的子类

  ```
  1==True
  0==False
  print(True+False)
  print(True-False)
  print(True*False)
  print(True/False)
  ```

# Python3错误与异常

### 1.异常处理  

- #### try/except语句  

  ```
  try:
  	执行代码
  except:
  	发生异常时执行的代码
  ```

  - try语句按照如下方式工作

  ```
  首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。
  
  如果没有异常发生，忽略 except 子句，try 子句执行后结束。
  
  如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
  
  如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。
  ```

  - 一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
  - 处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
  - 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组

  ```
  except(RuntimeError,TypeError,NameError):	
  	pass
  ```

  - 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出

  ```
  import sys
  
  try:
      f = open('myfile.txt')
      s = f.readline()
      i = int(s.strip())
  except OSError as err:
      print("OS error:{0}".format(err))
  except ValueError:
      print("Could not convert data to an integer.")
  except:
      print("Unexpeted error:",sys.exc_info()[0])
  ```

- #### try/except...else  

  ```
  try:
  	执行代码
  except:
  	发生异常时执行的代码
  else:
  	没有异常时的代码
  ```

  - 实例

  ```
  for arg in sys.argv[1:]:
      try:
          f=open(arg,'r')                 #在此判断文件是否可以打开
      except IOError:
          print('cannot open',arg)
      else:                               #如果打开文件时没有发生异常则执行else部分的语句
          print(arg,'has',len(f.readlines()),'lines')
          f.close()
  ```

- 使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到，而 except 又无法捕获的异常。

  异常处理并不仅仅处理那些直接发生在 try 子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。

  ```
  def this_fails():
      x=1/0
  
  try:
      this_fails()
  except ZeroDivisionError as err:
      print('Handling run—time error:',err)
  ```

-  #### try/finally语句  

  ```
  try:
  	执行代码
  except:
  	发生异常时执行的代码
  else:
  	没有异常时的代码
  finally:
  	不管有没有异常都会执行的代码
  ```

  - 实例

  ```
  try:
      runoob()
  except AssertionError as error:
      print(error)
  else:
      try:
          with open('file.log') as file:
              read_data = file.read()
      except FileNotFoundError as fnf_error:
          print(fnf_error)
  finally:
      print('这句话，无论异常与否都会执行。')
  ```

### 2.抛出异常  

- #### raise语法格式  

  ```
  raise [Exception [,args[,traceback]]]
  ```

  - 实例	

  ```
  x=10
  if x>5:
      raise Exception('x 不能大于5。x 的值为：{}'.format(x))
  ```

- raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是Exception 的子类）如果你这是想指定这是否抛出了一个异常，并不像去处理它，那么一个简单的raise语句就可以再次把它抛出。

  - 实例

  ```
  try:
      raise NameError('HiThere')  #模拟一个异常。
  except NameError:
      print('An exception flew by!')
      raise 
  ```

### 3.定义清理行为  

- try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。

  ```
  try:
      raise KeyboardInterrupt
  finally:
      print('Goodbye,world!')
  ```
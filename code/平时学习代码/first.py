
#input ("\n\n按下enter键后退出。")

x="a"
y="b"
#换行输出
print(x)
print(y)
print('----')
#不换行输出
print(x,end="")
print(y,end="")
print()

#import 与from...import
#命令行参数

#python允许同时为多变量赋值
a=b=c=1#从后向前赋值
#可以为多个对象指定多个变量
a,b,c=1,2,3

#Number
#type()函数可以用来查询变量所指的对象类型
q,w,e,r= 20, 5.5, True, 4+3j
print(type(q), type(w), type(e), type(r))
a=111
isinstance(a,int)
True
#type和isinstance的区别
#Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
#del语句

#数值运算
5+4         #加法
4.3-2       #减法
3*7         #乘法
2/4         #除法，得到一个浮点数
2//4        #除法，得到一个整数          # //得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
17%3        #取余
2**5        #乘方

#一个变量可以通过赋值指向不同类型的对象
#在混合计算时，python会把整型转换成浮点数
#Python 还支持复数，复数由实数部分和虚数部分构成，可以用 a + bj，或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。

#字符串的截取
#格式：变量【头下标：尾下标】（遵循左闭右开的原则）
str='123456789'

print(str)          #输出字符串
print(str[0:-1])    #输出第一个到倒数第二个的所有字符
print(str[0])       #输出字符串第一个字符
print(str[2:])      #输出从第三个开始后的所有字符
print(str[1:5:2])   #输出从第二个开始到 第五个且每隔一个 的字符
print(str * 2)      #输出字符串两次
print(str + '你好')  #连接字符串
print('hello\nrun') #转义特殊字符
print(r'hello\n')   #在字符串前加一个r,表示院士字符串，不会发生转义，r指raw，即raw string,会自动将反斜杠转义
print('\n')
print(r'\n')
#”\“还可作续行符

#Python 没有单独的字符类型，一个字符就是长度为1的字符串。
#Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
word='python'
print(word[0].word[5])
print(word[-1],word[-6])
#Python中的字符串不能改变
#比如 word【0】=‘m’会导致错误

#字符串运算符

#字符串格式化

#f-string
#称为字面量格式化字符串
#以f开头，后面跟着字符串，字符串中的表达式用{}括起来，它会将变量或表达式计算后的值替换进去
name = 'Runoob'
S=f'Hello {name}'          #替换变量
print(S)

w={'name':'Runoob','url':"www."}
s=f'{w["name"]}:{w["url"]}'
print(s)

#列表的截取
#格式：变量【头下标：尾下标】
#索引值以 0 为开始值，-1 为从末尾的开始位置
#‘+’是列表连接运算符，‘*’是重复操作

list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

#与Python字符串不一样的是，列表中的元素是可以改变的

#Python 列表截取可以接收第三个参数，参数作用是截取的步长，如果第三个参数为负数表示逆向读取
def reserseWords(input):
    #通过空格将字符串分隔符，将每个单词分隔成列表
    inputWords=input.split(" ")

    #翻转字符串
    #假设列表 list=[1,2,3,4],
    #list[0]=1,list[1]=2, 而-1表示最后一个元素 list[-1]=4(相当于list[3]=4)
    #inputWords[-1::-1]有三个参数
    #第一个参数-1表示最后一个元素
    #第二个参数为空，表示移动到列表末尾
    #迪桑参数为步长，-1表示逆向
    inputWords=inputWords[-1::-1]

    #重新组合字符串
    output=' '.join(inputWords)

    return output

if __name__ =="__main__":
    input='I like it'
    rw=reserseWords(input)
    print(rw)


#元组写在小括号 () 里，元素之间用逗号隔开。
#元组的元素不能修改,不许删除，但它可以包含可变的对象，比如 list 列表
#元组不可变是指，元组所指向的内存中的内容不可变

tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

#构造包含 0 个或 1 个元素的元组比较特殊
tup1=()     #空元组
tup2=(20,)  #一个元素，需要在元素后添加逗号

#set基本功能是进行成员关系测试和删除重复元素
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
#创建格式：parame={value01,value02,...}或者set(value)

sites={'Google','Taobao','Runoob','Facebook','Facebook'}
print(sites) #输出集合，重复的元素被自动去掉

#成员测试
if 'Runoob' in sites :
    print('Runoob在集合中')
else :
    print('Runoob 不在集合中')

#set可以进行集合运算
a=set('abracadabra')
b=set('alacazam')

print(a)
print(a-b)      #a 和 b的差集
print(a|b)      #a 和 b的并集
print(a&b)      #a 和 b的交集
print(a^b)      #a 和 b中不同时存在的元素

#列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#字典是一种映射类型，字典用 { } 标识，它的元素是键值对
# 格式：它是一个无序的  键(key) : 值(value)  的集合。
#键(key)必须使用不可变类型。在同一个字典中，键(key)必须是唯一的，即不可重复。
#创建空字典用{}

dict={ }
dict['one']="1-可"
dict[2]    ="2-可"

tinydict={'name':'runoob','code':1,'site':'www.'}

print(dict['one'])          #输出键为’one'的值
print(dict[2])              #输出键为2的值
print(tinydict)             #输出完整的字典
print(tinydict.keys())      #输出所有键
print(tinydict.values())    #输出所有值

dict([('ron',1),('Google',2),('Taobao',3)])
print(dict)


#隐式类型转换-自动完成
#Python 会将较小的数据类型转换为较大的数据类型，以避免数据丢失
#int&float
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

#int & string(会报错)
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))

print(num_int+num_str)

#显式类型转换
#int()强制转换为整型
x = int(1)   # x 输出结果为 1
y = int(2.8) # y 输出结果为 2
z = int("3") # z 输出结果为 3
#float()强制转换为浮点型
x= float(1)     # x 输出结果为 1.0
y = float(2.8)   # y 输出结果为 2.8
z = float("3")   # z 输出结果为 3.0
w = float("4.2") # w 输出结果为 4.2
#str()强制转换为字符串型
x = str("s1") # x 输出结果为 's1'
y = str(2)    # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'

num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("类型转换前，num_str 数据类型为:",type(num_str))

num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:",type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:",num_sum)
print("sum 数据类型为:",type(num_sum))

#列表推导式
#格式：【表达式 for变量 in列表】【out_exp_res for out_exp in input_list】
 #或者【表达式 for变量 if条件】【out_exp_res for out_exp in input_list if condition】
#out_exp_res：列表生成元素表达式，可以是有返回值的函数
#for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中
#if condition：条件语句，可以过滤列表中不符合条件的值

#实例：过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母
names = ['Bob','Tom','alice','Jerry','Wendy']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names)

#实例：计算 30 以内可以被 3 整除的整数
multiples=[i for i in range(30) if i%3==0]
print(multiples)

#字典推导式
#格式：【key-expr: value_expr for value in collection】
  #或者【key_expr: value_expr for value in collection if condition】

#实例：使用字符串及其长度创建字典
listdemo = ['Google','Runoob','Taobao']
#将列表中个字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key)for key in listdemo}
print(newdict)

#实例：提供桑数字，以三个数字为键，三个数字的平方为值来创建字典
dict={x:x**2 for x in (2,4,6)}
print(dict)
print(type(dict))


#集合推导式
#格式：{exoression for item in Sequence}
    #或者{expression for item in Sequence if conditional}

#实例：计算数字1，2，3的平方数
setnew={i**2 for i in (1,2,3)}
print(setnew)

#实例：判断不是abc的字母并输出
a={x for x in 'abracadabra' if x not in 'abc'}
print(a)
print(type(a))


#元组推导式
#格式：(expression for item in Sequence)
    #或者(expression for item in Sequence if condition)

#实例：使用下面的代码生成一个包含数字1~9的元组
a=(x for x in range(1,10))
print(a)       #<generator object <genexpr> at 00x000001C37ADF8890> # 返回的是生成器对象
print(tuple(a))#使用tuple()函数，可以直接将生成器对象转化为元组


#条件控制
#if实例

vary1 = 100
if vary1:
    print("1-if表达之条件为true")
    print(vary1)

vary2 = 0
if vary2:
    print("2-if 表达式条件为true")
    print(vary2)
print("Good bye!")

#狗的年龄计算判断
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

###退出提示
input("点击 enter 键退出")

#数字猜谜游戏
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

num=int(input("请输入一个数字："))
if num%2==0:
    if num%3==0:
        print("可以整除2和3")
    else:
        print("可以被2整除，不可以被3整除")
else:
    if num%3==0:
        print("可以被3整除，但是不能被2整除")
    else:
        print("不能整除2和3")

#match...case
#实例
mystatus=400
print(http_error(400))

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404|401|403:
            return "Not allowed"
        case 418:
            return "I am a teapot"
        case _:
            return "Something's wrong with the Internet"

#while循环
n=100

sum=0
counter=1
while counter <=n:
    sum+=counter
    counter+=1

print("1 到 %d 之和为： %d" % (n,sum))

#无限循环
var=1
while var==1:
    num =int(input("请输入一个数字："))
    print("你输入的数字是：",num)

print("Goodbye")

#while循环使用else语句
count = 0
while count < 5:
    print(count,"小于5")
    count=count+1
else:
    print(count,"大于或等于5")

#for循环
word='run'
for letter in word :
    print(letter)

#for...else
sites = ["Baidu","Google","Runoob","Taobao"]
for site in sites:
    if site=="Runoob":
        print("cainiao")
        break
    print("循环数据"+site)
else:
    print("没有循环数据！")
print("完成循环！")

n=5
while n>0:
    n-=1
    if n==2:
        continue
    print(n)
print('循环结束')

for letter in 'Runoob':
    if letter=='b':
        break
    print('当前字母为:',letter)


var = 10
while var > 0:
    print('当前变量值为：',var)
    var = var -1
    if var==5:
        break

print("bye")

#实例：查询质数
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'等于',x,'*',n//x)
            break
    else:
        #循环中没有找到元素
        print(n,'是质数')

#空语句实例
for letter in 'Runoob':
    if letter=='o':
        pass
        print('执行pass块')
    print('当前字母:',letter)



#异常处理
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

#try/except...else
for arg in sys.argv[1:]:
    try:
        f=open(arg,'r')                 #在此判断文件是否可以打开
    except IOError:
        print('cannot open',arg)
    else:                               #如果打开文件时没有发生异常则执行else部分的语句
        print(arg,'has',len(f.readlines()),'lines')
        f.close()

    #处理子句中调用的函数抛出的异常
    def this_fails():
        x=1/0

    try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handling run—time error:',err)

#Handling run-time error:int divison or modulo by zero

#try/finally语句
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


#抛出异常
x=10
if x>5:
    raise Exception('x 不能大于5。x 的值为：{}'.format(x))

try:
    raise NameError('HiThere')  #模拟一个异常。
except NameError:
    print('An exception flew by!')
    raise


#定义清理行为
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye,world!')

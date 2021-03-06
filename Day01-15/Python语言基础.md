# Python语言基础

## 搭建编程环境
**Windows环境**
打开[Python官方网站](https://www.python.org/downloads/)，下载相应版本的到Python安装程序到本地并安装，安装过程建议勾选“Add Python X.X.X to PATH”（将Python 添加到PATH环境变量）

## 运行Python程序

### 从终端运行Python程序

**确认Python的版本**

在终端或命令行提示符中键入下面的命令。

     python --version

也可以先输入python 进入交互式环境，再执行以下的代码检查Python的版本。

```Python
import sys
print(sys.version_info)
print(sys.version)
```
    
交互式编程不需要创建脚本文件，python解释器一次性执行命令窗输入的所有指令代码

### 执行Python脚本

使用文本编辑工具（Sublime、VSCode文本编辑工具），将需要执行的python代码编写成脚本文件XXX.py 保存起来，运行时只需要切换到脚本所在目录，执行

    python XXX.py
    
python解释器将一次性执行，脚本文件内的所有python代码。

## Python基础语法

### 代码注释

python中单行注释采用 # 开头，多行注释通常使用三个单引号(''')或三个双引号(""")
```Python
# 单行注释1
print('helloword') # 单行注释2
'''
多行注释1，使用单引号。
多行注释2，使用单引号。
'''  
"""
多行注释3，使用双引号。
多行注释5，使用双引号。
"""
```
    
### Python标识符

Python里的标识符由字母、数字和下划线( _ )组成
Python里所有变量以及函数的命名需要满足一下条件：

 1. 变量名和函数名由字母（广义的Unicode字符，不包括特殊字符）、数字、下划线组成，且开头不能为数字
 2. 不能与系统保留字符冲突

**Python 保留字符**

|and|or|not|import|class|from|
|:---:|:---:|:---:|:---:|:---:|:---:|
|if|elif|else|for|while|break|
|continue|print|pass|def|del|try|
|except|lambda|yield|in|is|with|
|return|global|raise|exec|assert|finally|

### 行与缩进

学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制，函数、循环以及其他逻辑判断。
python 最具特色的就是使用缩进来写模块。
缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。比如：

```Python
if True: 
     print "True" 
else: 
     print "False"
 ```

### 变量和数据类型

在程序设计中，变量是一种存储数据的载体。计算机中的变量是实际存在的数据或者说是存储器中存储数据的一块内存空间，变量的值可以被读取和修改，这是所有计算和控制的基础。计算机能处理的数据有很多种类型，除了数值之外还可以处理文本、图形、音频、视频等各种各样的数据，那么不同的数据就需要定义不同的存储类型。从Python3开始，python 总共支持6种标准数据类型：

#### 标准数据类型
1. **Number（数字）**
     * **整型**：Python中可以处理任意大小的整数（Python 2.x中有int和long两种类型的整数，但这种区分对Python来说意义不大，因此在Python 3.x中整数只有int这一种了），而且支持二进制（如0b100，换算成十进制是4）、八进制（如0o100，换算成十进制是64）、十进制（100）和十六进制（0x100，换算成十进制是256）的表示法。
     * **浮点型**：浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，浮点数除了数学写法（如123.456）之外还支持科学计数法（如1.23456e2）。
     * **布尔型**：布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来（例如3 < 5会产生布尔值True，而2 == 1会产生布尔值False）。
     * **复数型**：形如3+5j，跟数学上的复数表示一样，唯一不同的是虚部的i换成了j。
2. **String（字符串）**
     * **字符串**：字符串是以单引号或双引号括起来的任意文本，比如'hello'和"hello",可以书写成多行的形式（用三个单引号或三个双引号开头，三个单引号或三个双引号结尾），python中使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，也可以在字符串前面添加一个 r，表示原始字符串。
3. **List（列表）**
     * **列表**：列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。列表是写在方括号 [] 之间、用逗号分隔开的元素列表。和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
     列表截取语法为： 
```Python
     # 变量[头下标:尾下标:步长]
     # array[i:j:k] 

     array=['a','b','c','d','e','f']

     print(array) # 输出完整列表： ['a','b','c','d','e','f']
     print(array[0]) # 输出第一个元素：a
     print(array[0:3]) # 输出前3个元素 ：['a','b','c']
     print(array[1:3]) # 从第2个开始输出到第3个元素：['b','c']
     print(array[1:5:3]) # ['b','e']
     print(array*2) # 输出两次列表：['a','b','c','d','e','f','a','b','c','d','e','f']
```
4. **Tuple（元组）**
5. **Set（集合）**
6. **Dictionary（字典）**

在对变量类型进行转换时可以使用Python的内置函数

     int()：将一个数值或字符串转换成整数，可以指定进制。
     float()：将一个字符串转换成浮点数。
     str()：将指定的对象转换成字符串形式，可以指定编码。
     chr()：将整数转换成该编码对应的字符串（一个字符）。
     ord()：将字符串（一个字符）转换成对应的编码（整数）。

### 运算符
Python支持多种运算符

#### 算术运算符

| 运算符 | 功能 | 实例 |
| :---: | :---: | :---: |
| + | 加 | a+b 5+4=9 |
| - | 减 | a-b 6-3=3 |
| * | 乘 | a*b 2*3=6 |
| / | 除 | a/b 18/2=9 |
| % | 取模（取余）| a%b 9%5=4 |
| ** | 幂乘 | a**b a的b次幂 |
| // | 取整除 | 返回商的整数部分 |

#### 逻辑运算符

| 运算符 | 功能 | 实例 |
| :---: | :---: | :--- |
| and | 与 |  **x and y :** 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值 |
| or | 或 | **x or y :** 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。 |
| not | 非 | **not x :** 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True | 

#### 比较运算符

| 运算符 | 功能 | 实例 |
| :---: | :---: | :--- |
| == | 比较两个对象是否相等 | (a == b) 成立时返回True 否则返回False。 |
| != , <> | 比较两个对象是否不相等 | (a == b) 成立时返回False 否则返回True |
| > , >= | 大于，大于等于 | |
| < , <= | 小于，小于等于 | |

#### 赋值运算符

| 运算符 | 描述 | 实例 |
| :---: | :---: | :--- |
| = | 简单的赋值运算符 | c = a + b 将 a + b 的运算结果赋值为 c |
| += | 加法赋值运算符 | c += a 等效于 c = c + a | 
| -= | 减法赋值运算符 | c -= a 等效于 c = c - a | 
| *= | 乘法赋值运算符 | c *= a 等效于 c = c * a | 
| /= | 加法赋值运算符 | c /= a 等效于 c = c / a | 
| %= | 取模赋值运算符 | c %= a 等效于 c = c % a | 
| **= | 幂乘赋值运算符 | c **= a 等效于 c = c ** a | 
| //= | 整除赋值运算符 | c //= a 等效于 c = c // a | 

#### 身份运算符

| 运算符 | 描述 | 实例 |
| :---: | :---: | :--- |
| is | 判断两个标示符是否引用自同一个对象 | x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False|
| is not | 判断两个标识符是不是引用自不同对象 | x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。 |

#### 成员运算符

| 运算符 | 描述 | 实例 |
| :---: | :---: | :--- |
| in | 如果在指定的序列中找到值返回 True，否则返回 False | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。|
| not in | 如果在指定的序列中没有找到值返回 True，否则返回 False。 | x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。 |

#### 运算符优先级

下表列出了从最高到最低优先级的所有运算符：

| 运算符 | 描述  |
| :---: | :--- |
| **	| 指数 (最高优先级)|
| ~ + - |	按位取反, 一元加号和减号 (最后两个的方法名为 +@ 和 -@) |
| * / % // | 乘，除，取模和取整除 |
| + - | 加法减法 |
| >> << | 右移，左移运算符 |
| & | 位 'AND' |
| ^ \| | 位运算符 |
| <= < > >= | 比较运算符 |
| <> == != | 等于运算符 |
| = %= /= //= -= += *= **= |	赋值运算符 |
| is is not | 身份运算符 |
| in not in | 成员运算符 |
| not and or | 逻辑运算符 |

### 条件控制

Python 条件语句是通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块。比较其他语言Python在条件语言上有所不同，python语法上没有switch/case 语法，Python条件语法采用if else 来实现

```Python
''' 
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1) """
'''

x = float(input('please input x value：'))
if x > 1:
    y = 3*x-5
elif -1 <= x and x <= 1:
    y = x+2
else:
    y = 5*x+3
print('f(%.2f)=%.2f'%(x,y))

```

### 循环结构

使用循环结构我们可以轻松的控制某些事重复的发生，减少代码量，提高编写效率。Python中常用到的两种循环方式分别是 **for-in** 循环和 **while** 循环

#### for-in 循环

for-in循环可以精确控制循环次数，所以对于那些明确的知道循环执行的次数或者是要对一个容器进行迭代的应用场景，通常我们推荐使用for-in循环，如下列场景：实现1~100 数量求和：

```Python
'''
用for循环实现1~100求和
'''

sum = 0
for x in range(101):
    sum += x
print(sum)
```
说明：range() 是Python 的一个内置函数，可以创建一个整数列表，一般用在 for 循环中。

**range() 语法**
```Python
range(start, stop[, step])
```
* start: 计数从 start 开始。**默认是从 0 开始**。例如range（5）等价于range（0， 5）;
* stop: 计数到 stop 结束，但**不包括 stop**。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
* step：步长，**默认为1**。例如：range（0， 5） 等价于 range(0, 5, 1)

#### while 循环

如果要构造不知道具体循环次数的循环结构，推荐使用while循环，while循环通过一个能够产生或转换出bool值的表达式来控制循环，表达式的值为True循环继续，表达式的值为False循环结束。如下场景：“猜数字”的小游戏（计算机出一个1~100之间的随机数，人输入自己猜的数字，计算机给出对应的提示信息，直到人猜出计算机出的数字）。

```Python
"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

import random # 导入random库（生成随机数）

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)

```
上面代码中的 **break**关键字来提前终止循环，需要注意的是break只能终止它所在的那个循环，此外还有另一个关键字是 **continue**，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。

## Python函数和模块的使用

函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高应用的模块性，和代码的重复利用率。Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数

### 定义函数

在Python中可以使用def关键字来定义函数，和变量一样每个函数也有一个响亮的名字，而且命名规则跟变量的命名规则是一致的。在函数名后面的圆括号中可以放置传递给函数的参数，这一点和数学上的函数非常相似，程序中函数的参数就相当于是数学上说的函数的自变量，而函数执行完成后我们可以通过return关键字来返回一个值，这相当于数学上说的函数的因变量

#### 函数的参数

Python中的函数与其他语言中的函数还是有很多不太相同的地方，其中一个显著的区别就是Python对函数参数的处理。在Python中，函数的参数可以有默认值，也支持使用可变参数，所以Python并不需要像其他语言一样支持函数的重载，因为我们在定义一个函数的时候可以让它有多种不同的使用方式，例如：

```Python
import random

def roll_dice(n=2):
     """
    摇色子
    
    :param n: 色子的个数
    :return: n颗色子点数之和
    """
    
    total = 0
    for _ in range(n):
        total += random.randint(1, 6)
    return total
 

def add(a=0, b=0, c=0):
    """
    a+b+c
    """
    
    return a + b + c
```

```Python
# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())  # 0
print(add(1)) # 1
print(add(1, 2)) # 3
print(add(1, 2, 3)) # 6
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))  # 350
```

**不定长参数**

在具体业务场景中，有时需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，定长参数不同，不定长参数声明时不会命名。基本语法如下：

```Python
# 在参数名前面的*表示args是一个不定长参数
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
def printAnything(str1,*args):
    print(str1)
    print(args)
    return
    
printAnything('helloworld')  # helloworld
printAnything('helloworld',1,2,3,4,5) # helloworld (1,2,3,4,5)
printAnything('helloworld',1,2,3,4,5,helloworld) # helloworld (1,2,3,4,5,'helloworld')
```

### 模块管理

python程序的运行是基于python解释器来进行的，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。

**模块导入**

```Python
# 导入模块
import support
from modname import part1，part2...    # 从指定模块导入部分到当前命名空间
from modname import *    # 把一个模块的所有内容全都导入到当前的命名空间
```

一个模块只会被导入一次，不管执行了多少次import，相应模块也只会导入一次，Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。

**命名冲突**

例如：从模块module1中导入foo()方法，从模块module2中导入foo()方法

```Python
from module1 import foo
from module2 import foo

foo() # 由于由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义，所以这里执行的实际是module1.foo();

# 直接导入全部模块内容，根据模块选择执行内容
import module1 
import module2 

module1.foo()
module2.foo()

# 利用as解决命名冲突
import module1 as m1
import module2 as m2

m1.foo()
m2.foo()
```

**值得注意的一点** : 如果我们导入的模块除了定义函数之外还中有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是“__main__”。

module.py

```Python
def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
```

test.py
```Python
import module

# 导入module时 不会执行模块中if条件成立时的代码 因为模块的名字是module而不是__main__
```

## 字符串和常用数据结构

**字符串操作**

```Python
str1 = 'hello,world!'
# 通过len计算字符串的长度
print(len(str1)) # 12
# 将字符串首字母大写
print(str1.capitalize()) # Hello,world!
# 将字符串改写成大写
print(str1.upper()) # HELLO,WORLD!
# 从字符串中查找出子串的位置，字符串可视为字符数组，下标从0开始
print(str1.find('or')) # 7
print(str1.find('shit')) # -1
# 找出子串的索引，与find类似但找不到子串时会引发异常
print(str1.index('or')) # 7
# print(str1.index('shit'))  # 查找不到子串，报错
# 判断字符串是否以指定字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 判断字符串是否以指定字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定宽度居中并在两端填充指定字符,如果指定宽度小于字符串len，默认返回字符串本身
print(str1.center(50,'*')) # *******************hello,world!*******************
# 将字符串以指定宽度靠右放置，左侧填充指定字符串
print(str1.rjust(50,'*')) # **************************************hello,world!

str2 = 'abc12345'
# 从字符串中取出指定位置的字符
print(str2[0]) # a
# 字符串切片(从指定的开始索引到指定的结束索引，不包含结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c12345
# str2[i:j:k]，从索引i开始，一直到j(不包含j)，步长为k，进行切片
print(str2[2::2]) # c24
print(str2[::2]) # ac24
print(str2[::-1]) # 54321cba
print(str2[1:7:2]) # b13
print(str2[-3:-1]) # 34
# 检查字符串是全否由数字构成
print(str2.isdigit()) # False
# 检查字符串是否全由字母构成
print(str2.isalpha()) # False
# 检查字符串是否由字母和数字构成
print(str2.isalnum()) # True
print(str1.isalnum()) # False
# 去除字符串两边的空格
str3 = '  jackfrued@126.com '
print(str3.strip()) # jackfrued@126.com
```

**列表操作**
```Python
list1=[1,3,5,7,100]
list2=['hello']*5  # ['hello', 'hello', 'hello', 'hello', 'hello']

# 计算列表长度
print(len(list1)) # 5
# 下标取值
print(list1[0]) # 1
print(list1[4]) # 100
print(list1[-1]) # 取倒数第1个元素 100
print(list1[-3]) # 5
```
















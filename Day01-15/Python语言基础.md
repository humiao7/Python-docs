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

|and|or|not|
|---|---|---|
|exec|assert|finally|
|break|for|pass|
|class|from|print|
|continue|global|raise|
|def|if|return|
|del|import|try|
|elif|in|while|
|else|is|with|
|except|lambda|yield|

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

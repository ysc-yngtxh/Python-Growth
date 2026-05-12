#!/usr/bin/env python3

# 1.2.新手常见异常
# 异常类型                    通俗原因                             示例场景
# NameError              使用了没定义的变量
# SyntaxError            代码语法错（不符合Python 规则)        if 1 > 2（少了冒号）
# IndexError             索引/下标超出范围                    li = [1, 2, 3];      print(li[3])(最大索引是 2)
# ZeroDivisionError      除数为 0                           print(5/0)
# KeyError               字典里没有这个键                     info={"name":"小明"}  print(info["age"])
# IOError                文件操作失败（比如文件不存在）         尝试打开一个不存在的.txt 文件
# AttributeError         对象没有这个属性                     比如给字符串调用列表的 append方法
# ValueError             传入的值不对（类型对但内容无效）        int("abc") （字符串是文字，不能转整数）
# TypeError              类型不匹配                          1+"2"（数字和字符串不能相加）
# ImportError            导入模块失败（路径错或名字错）         import pandas123（模块名不存在）
# IndentationError       缩进错误（代码没对齐）                if 语句后没缩进，直接写 print


# try:
#     可能触发异常的代码块   # 尝试执行这段代码
# except［异常类型 as 交量名]:
#     异常发生时执行的代码块 ＃ 捕获到异常后，执行这里的处理逻辑
# else：
#     无异常时执行的代码块  ＃没发生异常，才执行这里
# finally：
#     无论是否异常都执行的代码块 ＃ 不管有没有异常，最后都会执行


# 异常处理（捕获异常），Exception 是所有非语法类异常的父类
try:
    num = int(input("请输入一个数字："))  # 输入数字没问题，但是输入其他字符就会报错
    print(num2)
except (ValueError, NameError):        # 使用元组指定多种异常，使用同一种逻辑处理
    print("发生错误！可能是输入不对或变量没定义")
print("================")


try:
    num = int(input("请输入一个数字："))  # 输入数字没问题，但是输入其他字符就会报错
    print(num2)
except ValueError:        # 使用元组指定多种异常，使用同一种逻辑处理
    print("输入错误！请输入纯数字字符！")
except NameError:        # 使用元组指定多种异常，使用同一种逻辑处理
    print("发生错误！存在变量没定义")
print("================")


try:
    num = int(input("请输入一个数字："))  # 输入数字没问题，但是输入其他字符就会报错
    print(num2)
except Exception as e:
    print(e)
else:
    print("执行成功")
finally:
    print("无论如何都会执行的代码块")
print("================")


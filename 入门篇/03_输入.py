#!/usr/bin/env python3

# 注意：不论用户在控制套输入什么样的数据，最后 input 函数都会把它当成字符串来处理。
name = input("请输入任意内容：")
print(name, "你好～", type(name))

# 通过类型方法将输入内容转换为执行的类型：int()、float()、bool()、str()等。
a = int(input("请输入一个整数："))
b = float(input("请再输入一个整数："))
print(a, "+", b, "=", a + b, type(a + b))

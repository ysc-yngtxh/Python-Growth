#!/usr/bin/env python3

# TODO 定义：变量名 = 值
sum = 3 * 4
print("sum =", sum)

# 变量的值可以反复赋值（后赋值会覆盖），并且可以是不同类型。
variable = 100
variable = 3.14
variable = "游家纨绔"
print("variable =", variable)

# 可同一行中定义多个变量
Java,C,Python="精通","专研","学习"
print("Java =", Java)
print("C =", C)
print("Python =", Python)


# TODO 基本数据类型
# 1、数值类型
# 1.1、整数（int）
a = 100
print("a =", a, type(a))
# 1.2、浮点数（float）
b = 3.14
print("b =", b, type(b))
# 1.3、复数（complex）【了解即可】
c = 1 + 2j
print("c =", c, type(c))
# 1.4、布尔型
print("True =", True, type(True))
print("False =", False, type(False))

# 2、字符串（str）
# 2.1、单行字符串，单引号/双引号 都表示字符串类型
print("s =", "Hello, World!", type("Hello, World!"))
print("s =", 'Hello, World!', type('Hello, World!'))
# 2.2、多行字符串
print("""
你好～
我是游家纨绔！
天命所归
""")
# 2.3、空值（None）：表示什么都没有
print("None =", None, type(None))

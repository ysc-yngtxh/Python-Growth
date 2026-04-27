#!/usr/bin/env python3

# 定义函数：函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。函数能提高应用的模块性，和代码的重复利用率。
# 函数语法：def 函数名(参数列表):

# 1、普通函数示例：
print("-----------------------------------1-----------------------------------")
# tea_type、sweetness是函数的形参（形参是定义函数时指定的参数，用于接收函数调用时传递的值）
def make_tea(tea_type="绿茶", sweetness=1):
    print(f"泡一杯{tea_type}，甜度为{sweetness}")
# 调用函数，传入实参（实参是函数调用时传递给函数的值）
make_tea()        # 使用默认参数值
make_tea("红茶")  # 指定茶的类型，使用默认甜度
make_tea("乌龙茶", 2)  # 指定茶的类型和甜度


# 2、可变参数
print("-----------------------------------2-----------------------------------")
# 可变参数：*args（只有加上 * 符号的形参才是可变参数）接收任意数量的参数，以元组的形式保存
def sum_(*args):
    print(args, type(args))
    # 定义变量保存总和
    result = 0
    # 从元组中拿出一个个元素 --> 遍历for循环
    for num in args:
        print(num)
        result += num
    print("---")
    # 计算结果 = 计算结果 + 拿出来的数字
    print("总和:", result)

sum_(1, 2, 3)
sum_(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# 3、关键字可变参数
print("-----------------------------------3-----------------------------------")
# 关键字可变参数（**kwargs)核心规则：接收任意数量的"键=值"形式的参数，自动打包成字典。
# 适用场景：函数需要处理可选的关键字参数（比如用户注册，必填用户名，可选年龄、性别等）。
def create_user(username, **kwargs):
    """创建用户: username是必填项，其他是可选项"""
    print("用户名：", username)
    # 遍历可选参数（kwargs是字典）
    for key, value in kwargs.items():
       print(f"可选信息：{key}={value}")
    for i in kwargs.items():
       print(f"可选信息：{i[0]} = {i[1]}")

create_user("bingbing")                            # 只传必填项
create_user("bingbing", age=18, sex="女") # 传必填 + 2个可选
create_user("bingbing", height=1.75, weight=60, qq="123456") # 传必填 + 3个可选


# 4、返回值
print("-----------------------------------4-----------------------------------")
# 4.1、返回单个值场景：函数需要返回一个明确结果(比如判断是否为偶数、计算面积)。
def return_value():
    return "游家纨绔"
print(return_value(), type(return_value()))
# 4.2、返回多个值(实际返回元组)场景：需要同时返回多个相关结果（比如返回坐标、返回统计数据）。
def return_value2():
    return "green", "游家纨绔", 29
print(return_value2(), type(return_value2()))


# 5、接收方式
print("-----------------------------------5-----------------------------------")
def received(a, b):
    sum_value = a + b
    mul_value = a * b
    return sum_value, mul_value
# 5.1、使用一个变量接收（得到元组）
result = received(1, 2)
print(result)
# 5.2、解包，使用多个变量接收
retrieve_sum, retrieve_mul = received(1, 2)
print(f"和：{retrieve_sum}\n积：{retrieve_mul}")


# 6、变量作用域
print("-----------------------------------6-----------------------------------")
ext_value = 0.1
ext_value2 = 0.1
def variable_scope():
    ext_value = 0.5   # 局部变量。在函数中定义，只能在函数中使用
    global ext_value2 # 使用 global 关键字，声明为全局变量。
    return ext_value, ext_value2
print(ext_value, ext_value2)
print(variable_scope())


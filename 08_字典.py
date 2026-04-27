#!/usr/bin/env python3

# 1、定义字典（存储用户信息）
info = {"姓名": "游家纨绔", "性别": "男", "身高": 180, "体重": 85, "爱好": "学习"}
print(info, type(info))
print(info["姓名"], info["性别"], info["身高"], info["体重"], info["爱好"])

# 2、键值 Key 必须唯一；如果重复，后面的值覆盖掉前面的
dic = {"name": "孙悟空", "name": "美猴王"}
print(dic, type(dic))

# 3、获取字典值
# 方式一：通过索引获取
# print(info["别名"])  这种方式存在一个致命问题：当取的 key 不存在时，会抛出异常
# 方式二：通过 get() 方法获取
print(info.get("别名"))                          # 当取的 key 不存在时，默认返回 None
print(info.get("别名", "没有这个键"))  # 当取的 key 不存在时，返回指定的默认值

# 4、更新字典
data = {"username": "Jack", "sex": "boy", "age": 29, "tel": 19237800789}
print(data, type(data))

# 5、删除字典
print(data.pop("sex"), type(data))
# data.pop("number")  # 删除不存在的键会报错
# 删除不存在的键会报错，因此可以指定返回的默认值，避免报错
print(data.pop("number", "number键不存在"), type(data))
print(data.popitem(), type(data))
print(data.clear(), type(data))  # clear() 方法会清空字典，但不会删除字典对象

#  6、遍历
print(info.keys())
print(info.values())
print(info.items())
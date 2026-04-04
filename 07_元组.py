#!/usr/bin/env python3

# 元组和列表最大的区别：元组创建后，不能添加、删除或直接修改元素。

# 1、定义元组
weekdays = ("周一", "周二", "周三", "周四", "周五", "周六", "周日")
print(weekdays, type(weekdays))
print(weekdays[0])
print(weekdays[1:4])
print(weekdays[-1])
print(weekdays[-3:-1])
print(weekdays[-3:1]) # 由于默认的步长是正数，所以取值会从左往右取，但是这个时候 结束索引 位于 开始索引 之前，所以返回的是空值
print(weekdays[-3:1:-2]) # 定于负数步长，取值会从右往左取，合理取到值

# 2、注意⚠️：当定义的元组中只有一个元素时，必须在元素后面添加逗号，否则 Python 会将其识别为普通的括号表达式，而不是元组。
tup = (1)
print(tup, type(tup))
tup2 = (1,)
print(tup2, type(tup2))

# 3、元组常见的内建函数
print(len(weekdays))         # 计算元组中元素的个数
print(weekdays.count("周一")) # 统计元组中某个元素出现的次数
print(weekdays.index("周三")) # 返回元组中某个元素的第一个匹配项的索引位置，如果没有找到该元素，则会引发 ValueError 错误
print("周八" in weekdays)     # 判断某个元素是否在元组中，返回 True 或 False
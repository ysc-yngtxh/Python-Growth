#!/usr/bin/env python3

# 集合是 Python 中特殊的“数据容器”。
# 核心特点：无序 ＋ 元素唯一 ，能自动去掉重复数据。
# 还能快速做交集、并集等集合运算，适合去重、数据对比等场景。学会运用集合，能高效解决重复数据处理问题，简化数据对比逻辑。

# 1、定义集合（自动去重）
a = {'a', 'a', 'a', 'b', 'c', 'd'}
print(a, type(a))
# 2、定义空集合：与定义空字典有区别
b = {}      # 定义的是空字典
print(b, type(b))
c = set()   # 定义的是空集合
print(c, type(c))

# 集合是无序的，没有索引，不能像 列表、元组 那样通过下标获取元素
# 集合元素类型限制：只能存不可变类型（数字、字符串、元组），不能存列表、字典等可变类型。


# 3、集合常见的内建函数
data = {1, 2, 3, 4, 5}
# 3.1、向集合添加单个元素，元素已存在会被自动去重
data.add(6)
print(data, type(data))
# 3.2、向集合添加多个元素
data.update("123")
data.update((7, 8, 9))
print(data, type(data))
# 3.3、从集合中删除元素，元素不存在会报错
data.remove('1')
print(data, type(data))
# 3.4、从集合中删除元素，元素不存在不会报错【推荐】
data.discard('2')
print(data, type(data))
# 3.5、从集合中随机删除一个元素并返回，集合为空会报错
data.pop()
print(data, type(data))
# 3.6、清空集合元素
data.clear()
# 3.7、其他方法
data = {1, 2, 3, 4, 5}
print(len(data))     # 集合元素个数
print(max(data))     # 集合元素最大值
print(min(data))     # 集合元素最小值
print(sum(data))     # 集合元素求和
print(sorted(data))  # 集合元素排序，返回列表
print(sorted(data, reverse=True))  # 集合元素逆序排序，返回列表


# 4、集合交集、并集
i1 = {1, 2, 3, 4, 5, 6}
i2 = {4, 5, 6, 7, 8}
i3 = {4, 5, 7, 8, 9, 10}
# 4.1、交集：返回两个集合中都存在的元素
print(i1 & i2)                               # 交集：{4, 5, 6}
print(i1.intersection(i2))                   # 交集：{4, 5, 6}
print(i1.intersection(i2, i3))           # 交集：{4, 5}
print(i1.intersection(i2).intersection(i3))  # 交集：{4, 5}
# 4.2、并集：返回两个集合中所有存在的元素（去重）
print(i1 | i2)                 # 并集：{1, 2, 3, 4, 5, 6, 7, 8}
print(i1.union(i2))            # 并集：{1, 2, 3, 4, 5, 6, 7, 8}
print(i1.union(i2, i3))    # 并集：{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(i1.union(i2).union(i3))  # 并集：{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 4.3、差集：返回在第一个集合中存在但在第二个集合中不存在的元素
print(i1 - i2)            # 差集：{1, 2, 3}
print(i1.difference(i2))  # 差集：{1, 2, 3}
# 4.4、对称差集：返回在两个集合中存在但不同时存在的元素
print(i1 ^ i2)            # 对称差集：{1, 2, 3, 7, 8}
#!/usr/bin/env python3

# 1、一维列表
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array[2])
print(array[:4])
print(array[::5])
print(array[-2])
print(array[-2:2])    # 由于默认的步长是正数，所以取值会从左往右取，但是这个时候 结束索引 位于 开始索引 之前，所以返回的是空值
print(array[-2:2:-2]) # 定于负数步长，取值会从右往左取，合理取到值

# 2、多维列表
array2 = [[1,2,3], [4,5,6], [7, 8, 9, 10]]
print(array2[2][3])

# 3、列表常见的内建函数
# 3.1、插入函数
array.append(100)
print(array)
# 3.2、插入可迭代数据的函数
array.extend([200, 300])
array.extend("abcd")
print(array)
# 3.3、插入指定位置的函数
array.insert(10, 50)
print(array)
# 3.4、删除函数
array.remove('a') # 删除不存在的数据会报错
array.remove("b") # 删除不存在的数据会报错
array.remove("c") # 删除不存在的数据会报错
array.remove("d") # 删除不存在的数据会报错
print(array)
# 3.5、删除末尾数据函数
array.pop()
print(array)
# 3.6、反序函数
array.reverse()
print(array)
# 3.7、排序函数
array.sort()
print(array)
# 3.8、统计函数
print(array.count(100))
# 3.9、索引函数
print(array.index(5)) # 不存在索引的数据会报错

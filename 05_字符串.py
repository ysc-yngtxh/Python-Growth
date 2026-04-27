#!/usr/bin/env python3

# 1、字符串的拼接
str1 = "美女，"
str2 = "你好啊！"
str3 = "方便加个 VX 么"
print(str1 + str2 + str3)
# print(str1 + 18) 该写法报错：原因为 18是整数类型，无法与字符串类型进行拼接

# 2、字符串重复（*）指定字符串重复的次数
print(str1 * 3)

# 3、成员运算法（in/not in）
print("你" in str2)     # 输出：True（包含“你”）
print("你" not in str2) # 输出：False（包含“你”）

# 4、索引（下标）
a = "我乃花果山水帘洞美猴王齐天大圣孙悟空～"
# 从左往右，从 0 开始
print(a[0])
print(a[1])
print(a[2])
print(a[3])
# 从右往左，从 -1 开始
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])

# 5、切片：字符串【起始索引:结束索引:步长】
# 5.1、指定起始索引
print(a[:])    # 没有指定，表示从头切到尾
print(a[2:])   # 从索引 2 开始，切到字符串末尾
# 5.2、指定结束索引
print(a[:5])   # 从索引 0 开始，切到索引 5（不包含索引 5）
print(a[2:5])  # 从索引 2 开始，切到索引 5（不包含索引 5）
# 5.3、指定步长：正数从左往右，负数从右往左
print(a[::2])   # 从头到尾，步长为 2
print(a[1::2])  # 从索引 1 开始到末尾，步长为 2
print(a[::-1])  # 从头到尾，步长为 -1，即反转字符串

# 6、原始字符串（r）
print("C:\\new\\test\\text.txt")  # 输出：C:\new\test\text.txt
print(r"C:\\new\\test\\text.txt")    # 输出：C:\new\test\text.txt

# 7、格式化字符串（f）
print("我叫%s，今年%d岁了！" % ("小明", 18))  # 使用 %s 和 %d 占位符
name = "小明"
age = 18
print("我叫%s，今年%d岁了！" % (name, age))            # 使用变量进行格式化
print("我叫{}，今年{}岁了！".format("小明", 18))  # 使用 {} 占位符和 format 方法
print("我叫{}，今年{}岁了！".format(name, age))  # 使用变量进行格式化
print(f"我叫{name}，今年{age}岁了！")                  # 使用 f-string 进行格式化

# 8、数字格式化
sid = 1
print("他的学号是：123")
print(f"我的学号是：{sid:3}")  # 设置最小宽度为 3（默认往前补空格）
print(f"我的学号是：{sid:03}") # 设置最小宽度为 3（定义往前补数字 0）
pi = 3.1415926
print(f"保留10位小数：{pi:.10f}") # 设置最小宽度为 3（定义往前补数字 0）
print(f"保留3位小数：{pi:.3f}")   # 遵循四舍五入原则

# 9、对齐与填充
userName = "游家纨绔"
print(f"用户名：{userName:>10}")  # 右对齐，宽度为 10，默认填充空格
print(f"用户名：{userName:<10}")  # 左对齐，宽度为 10，默认填充空格
print(f"用户名：{userName:^10}")  # 居中，宽度为 10，默认填充空格
print(f"用户名：{userName:*>10}") # 右对齐，宽度为 10，填充字符为 *
print(f"用户名：{userName:*<10}") # 左对齐，宽度为 10，填充字符为 *
print(f"用户名：{userName:*^10}") # 居中，宽度为 10，填充字符为 *

# 10、字符串常见的内建函数
# 10.1、find()
str = "QWERty uiopasd\nhfklKg \tnmczxbvaaQQ"
print(str.find("a"))    # 输出：10（找到第一个 a 的索引位置）
print(str.find("11"))   # 输出：-1（没有找到 11）
# 10.2、index()
print(str.index("a"))   # 输出：10（找到第一个 a 的索引位置）
# print(str.index("11"))  # 报错：没有找到 11，抛出 ValueError 异常
# 10.3、count()
print(str.count("a"))   # 输出：1（字符串中 a 出现的次数）
print(str.count("z"))   # 输出：1（字符串中 z 出现的次数）
# 10.4、replace()
print(str.replace("a", "A"))           # 输出：QWERty uiopAsd\nhfklkg \tnmczxbvaaQQ（将第一个 a 替换为 A）
print(str.replace("a", "A", 2))  # 输出：QWERty uiopAsd\nhfklkg \tnmczxbvAaQQ（将前两个 a 替换为 A）
# 10.5、split()
print(str.split())                     # 默认使用空白（空格、\n、\t）进行分割
print(str.split(" ",  2))  # 分割两次
# 10.6、strip()
print(str.strip())           # 默认去除首尾空白（空格、\n、\t）
print(str.strip("Q"))        # 去除 首尾字符'Q'
# 10.7、upper()、lower()、title()
print(str.upper())  # 输出：QWERTY UIOPASD\nHFKLKG \TNMCZXBVAA（将字符串中的所有字母转换为大写）
print(str.lower())  # 输出：QWERTY UIOPASD\nHFKLKG \TNMCZXBVAA（将字符串中的所有字母转换为大写）
print(str.title())  # title()：方法将每个单词的首字母转换为大写，其余字母转换为小写。
# 10.8、startswith()、endswith()、isupper()、islower()
print(str.startswith("q"))
print(str.endswith("QQ"))
print(str.isupper())
print(str.islower())



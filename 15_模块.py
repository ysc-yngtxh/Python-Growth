#!/usr/bin/env python3

# 导入 random 模块
import random
# 需求：生成 1 到 100 之间的随机整数
# 调用random模块里面的 randint函效
num = random.randint(1, 3)
print (num)


import requests
response = requests.get("https://www.baidu.com")
response.encoding = "utf-8"
print(response.text)


# TODO 引入自定义模块。方式一：import 模块名 或 import 模块名 as 别名（别名可选，简化书写）
import my_tools as mt
# 使用功能：模块名.功能
print(mt.add(1, 2))
mt.greet("小明")
print(mt.module_name)


# TODO 引入自定义模块。方式二：from 模块名 import 函数名/变量名/类名（可导入多个，用逗号分隔）
from my_tools import add, module_name
# 使用功能：功能
print(add(1, 2))
print(module_name)


# TODO 引入自定义模块。方式三：from 模块名 import * （* 表示 “所有”）
from my_tools import *
# 使用功能：功能
print(add(1, 2))
greet("小红")
print(module_name)

# 注意事项：
#    1、模块只导入一次：同一个模块在程序中只需导入一次，首次导入后会加载到内存，后续导入不会重复加载（节省资源，避免冲突）。
#    2、两个模块有同名功能时，用“模块名.功能名”区分，或用 as设别名。
#    3、尽量不用 from 模块名 import *，容易覆盖当前文件的变量/函数。

#!/usr/bin/env python3

# 一、包的核心标志： __init__.py 文件
# 一个文件夹要被 Python 识别为包，必须包含 __init__.py 文件（Python3.3+可省略，但建议保留，明确告诉Python“这是个包”）。
# 这个文件的 3 个核心作用：
#   1、标识目录为包：告诉 Python 这个文件来不是普通文件夹，而是包。
#   2、控制导入范围：通过_all 变量，指定批量导入时要包合的模块。
#   3、执行初始化操作：导入包时，会自动执行这个文件里的代码（比如初始化变量、导入必要模块）。


# 方式一：import 包名.模块名 -- 精准导入指定模块
import my_package.calc
# 使用功能：包名.模块名.功能
print(my_package.calc.add(8, 3))

# 方式二：from 包名.模块名 import 功能 -- 直接导入模块中的功能
from my_package.calc import add
print(add(5, 3))

# 方式三：from 包名 import 模块名 -- 简化导入模块
from my_package import calc
print(calc.add(11, 3))

# 方式四：from 包名 import * -- 批量导入（需要在 __init__.py 文件中配置 __all__）
from my_package import *
print(calc.add(28, 3))
greet.say_hello("小明")

# 方式五：from 包名.模块名 import * -- 批量导入模块中的功能（需要在模块文件中配置 __all__）
from my_package.calc import *
print(add(100, 4))
# print(subtract(10, 4))  由于 calc.py 中 __all__ 只包含 add 和 multiply，所以 subtract 不会被导入，无法使用。


# 导入包的注意事项
#   1、包名/模块名不能冲突：不能和内置模块、已安装的第三方模块重名（比如不能叫 requests 包，会和第三方模块冲突）。
#   2、__init__.py 别写复杂代码：这个文件主要用于标识包和控制导入，写太多复杂逻辑会影响导入效率，还容易出错。
#   3、导入语句建议写在文件开头：方便阅读和组织代码，符合 Python 编程习惯。
#   4、层级不要太深：包的嵌套尽量不超过3层（比如 包1.包2.包3.模块 ），否则导入路径太长，不方便使用。
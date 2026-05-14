#!/usr/bin/env python3

# 变量
module_name = "工具模块™"

# 函数
def add(a, b):
    return a + b


def greet(name) :
    print(f"你好呀，{name}!")


# 在本模块中执行，那么 __name__ 的值是 "__main__"；
# 但是在其他模块中导入 my_tools 模块，那么 __name__ 的值是 "my_tools"
print("my_tools.py模块中内置全局变量__name__: ", __name__)

# 隐私代码，只在本模块执行，可避免在被其它模块导入时执行
if __name__ == "__main__":
    # 测试代码：测试功能是否正常，可以使用 print(add(3, 5)) 来测试add函数
    print(add(3, 5))
    print(module_name)
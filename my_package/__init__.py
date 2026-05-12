print("我是 __init__.py")

# __all__ 变量的详细用法
# __all__ 是一个列表，专门控制 from ••• import * 的导入范围，避免导入不必要的内容：
# •作用在包的 __init__.py 里：指定 from 包名 import * 时要导入的模块；
# •作用在模块里：指定 from 模块名 import * 时要导入的 类/函数/变量。
__all__ = ["greet", "calc"]  # 指定批量导入时要包含的模块
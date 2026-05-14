#!/usr/bin/env python3

# 1、创建异常对象：异常类型（异常具体描述信息）
# e = Exception("余额不足！")
# 2、抛出异常：raise 异常对象
# raise e


# 需求：模拟银行取款场景
# 账户余额和状态
balance = 1000     # 余额 1000（全局变量）
is_frozen = False  # 账户是否冻结（False没有冻结，True 冻结）

# 实现一个功能的代码块 ==> 函数
def withdraw(amount):
    global balance
    # 先判断账户是否冻结
    if is_frozen:
        # 账户冻结 ==> 抛出异常
        raise Exception("账户已冻结！")
    # 再判断余额是否充足：
    if balance < amount:
        # 余额不足 ==> 抛出异常
        raise Exception(f"余额不足！当前余额：{balance}元。")
    # 取款：余额-余额-取款金额
    balance -= amount
    print(f"当前余额：{balance}元。")

withdraw(200)
withdraw(2000)
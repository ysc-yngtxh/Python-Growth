#!/usr/bin/env python3

number = int(input("请输入一个数字："))
if 100>number>0 and number%2==0:
    print("您输入的数字是偶数")
elif number<0 or number==0:
    print("您输入的数字小于等于零，输入不规范")
elif number == 100:
    print("哇哦～恭喜你输入了一个幸运数字～")
elif not number%2==0:
    print("您输入的数字是奇数")
print("程序结束")



# 使用递归计算阶乘

i = int(input("请输入一个整数:"))


def fun(var):
    if var < 1:
        print("输入有误")
    else:
        if var == 1:
            return 1
        else:
            return var * fun(var - 1)


if type(fun(i)) is int:
    print(f"{i}的阶乘为：", fun(i))


def t(var):
    print("t:", var)
    if var == 0:
        print("over")
    else:
        t(var - 1)

    print("*****t:", var)


t(4)

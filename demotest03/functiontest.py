import copy


def fun(var):
    s = 1
    for x in range(1, var + 1):
        s *= x
    print(f"{var}的阶乘为：{s}")


# fun(5)
# fun1 = fun
# fun1(6)
# fun(7)
for x in range(1, 11):
    fun(x)


def copyTest():
    a = [10, 20, [30, 40]]
    b = copy.copy(a)
    print(a)
    print(b)
    b.append(30)
    b[2].append(50)
    print(a)
    print(b)


print("-------------------copy()----------------")
copyTest()


def deepCopyTest():
    a = [10, 20, [30, 40]]
    b = copy.deepcopy(a)
    print(a)
    print(b)
    b.append(30)
    b[2].append(50)
    print(a)
    print(b)


print("---------------deepcopy()----------------------")
deepCopyTest()

print("---------------------------------------------------------")
f = lambda a, b, c: a ** 2 + b ** 2 + c ** 2
print(f)
print(f(2, 3, 4))

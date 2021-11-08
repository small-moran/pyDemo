# 列表的创建
import random

l1 = [1, 2, 3, "hello"]
l2 = []

ll1 = list()
print(ll1)  # []
ll2 = list("hello python")
print(ll2)  # ['h', 'e', 'l', 'l', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n']
ll3 = list(range(10))
print(ll3)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(type(range(2, 10)))  # <class 'range'>
ll4 = list(range(2, 10))
print(ll4)  # [2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(10, 2, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3]
print(list(range(3, -5, -2)))  # [3, 1, -1, -3]

li1 = [x for x in range(5)]
print(li1)  # [0, 1, 2, 3, 4]

print([x ** 2 for x in range(2, 5)])  # [4, 9, 16]

print([x ** 2 for x in range(2, 10) if x % 3 == 0])  # [9, 36, 81]

l1 = l1 + [9, 8, 7]
print(l1)

a = [1, 2, 3]
a = a * 3
print(a)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

print(a.pop(1))
print(a)

a.remove(2)
print(a)
a = [1, 3, 1, 3, 1, 2, 3]
print(a.index(3))  # 1 从头查找第一个3所在的索引位置
print(a.index(3, 2))  # 3 从索引为2的元素开始查找第一个3所在的位置
print(a.count(2))

print(a[1:4])
for x in a:
    print(x)

a.sort()
print(a)
a.sort(reverse=True)
print(a)
random.shuffle(a)
print(a)
b = sorted(a)
print(b)
print(sorted(a, reverse=True))

a = [1, 2, 3, 4]
# 方式一：slice切片
b = a[::-1]
print(b)
# 方式二
c = sorted(a, reverse=True)
print(c)
# 方式三
d = reversed(a)
e = list(d)
print(d)  # <list_reverseiterator object at 0x000001ED229FCB20>
print(e)

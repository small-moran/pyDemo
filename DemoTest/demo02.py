a = 10.0
b = 10
print(a is b)
print(a == b)

c = -61111111.2
d = -61111111.2
print(c is d)
# ord():将字符转换成unicode编码
print(ord('张'), ord('成'), ord('奎'))
# chr()：将unicode转换成字符

a = 'aa' + ' bb'
print(a)  # aa bb
c = a * 3
print(c)  # aa bbaa bbaa bb

# name = input("请输入姓名：")
# print(name)

s = "hello python"
s1 = s.replace("python", "world")
s2 = s.replace("he", "we")
print(s)  # hello python
print(s1)  # hello world
print(s2)  # wello python

ss = "0123456789"
# print(ss[:])  # 0123456789
# print(ss[2:])  # 23456789
# print(ss[:2])  # 01
# print(ss[2:7])  # 23456
# print(ss[2:7:1])  # 23456
# print(ss[2:7:2])  # 246

print(ss[-3:])  # 789
print(ss[-8:-3])  # 23456
print(ss[-8:-3:2])  # 246

print(ss[::-1])  # 9876543210

ss1 = "to be or not to be"
print(ss1.split())  # ['to', 'be', 'or', 'not', 'to', 'be']

str1 = ["hadoop", "mr", "spark"]
print("*".join(str1))  # hadoop*mr*spark
print(" ".join(str1))  # hadoop mr spark

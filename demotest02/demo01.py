import math

if None:
    print(math.e)
else:
    print(not None)

# num = int(input("请输入一个数："))
# out = num if num > 0 else -num
# print(out)

num = 0
while num <= 10:
    print(num, end="\t")
    num += 1
print("\n")

print("------------------------------------")

num = 0
su = 0
while num <= 100:
    su += num
    num += 1
print(su)
print("--------------------------------------------")

num = su = 0
while num <= 100:
    if num % 2 == 0:
        su += num
    num += 1
print(su)

print("--------------------------------------------")

num = su = 0
while num <= 100:
    if num % 2 == 1:
        su += num
    num += 1
print(su)


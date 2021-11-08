a = (10, 20, 30)
b = 10, 20, 30
print(type(a))
print(b)
t1 = tuple([1, 2, 3])
t2 = tuple(range(5))
t3 = tuple("abcd")
print(t1, t2, t3)
l1 = [1, 2]
l2 = [9, 8]
l3 = [5, 6]
print(list(zip(l1, l2, l3)))  # [(1, 9, 5), (2, 8, 6)]

tup1 = (x ** 2 for x in range(5))  # tup1 是一个迭代器
tup2 = tuple(tup1)
print(tup2)  # (0, 1, 4, 9, 16)
print(list(tup1))  # [] 原因：迭代器只能使用一次

d1 = {"name": "spike", "age": 18}
d2 = dict(name="Tom", age=88)
d3 = dict([("name", "Jack"), ("ege", 66)])
d4 = [("name", "Jack"), ("ege", 66)]
print(d1)
print(d2)
print(d3)

k = ["name", "ege"]
v1 = ["Jerry", 14]
v2 = ["Luce", 26]
d5 = dict(zip(k, v1))
d6 = dict(zip(k, v2))
print(d5, d6)

d7 = dict.fromkeys(["name", "ege", "job"])
print(d7)  # {'name': None, 'ege': None, 'job': None}

d1 = {"name": "tom", "ege": 88, "job": "cat"}
print(d1["name"])
print(d1.get("name"))

print(d1.keys())  # dict_keys(['name', 'ege', 'job'])
print(d1.values())  # dict_values(['tom', 88, 'cat'])
print(len(d1))  # 3

d1 = {"name": "tom", "ege": 88, "job": "cat"}
d1["nation"] = "USA"
d1["age"] = 86

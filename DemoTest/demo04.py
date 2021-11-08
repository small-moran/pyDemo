import io

a = "名字是：{0}，年龄为：{1}"
b = a.format("Spike", 18)
print(b)  # 名字是：Spike，年龄为：18

a1 = "名字是：{name}，年龄为：{age}"
b1 = a1.format(name="张学友", age=58)
print(b1)  # 名字是：张学友，年龄为：58

a2 = "名字是：{0}，年龄为：{1},{0}真的很帅"
b2 = a2.format("Spike", 18)
print(b2)  # 名字是：Spike，年龄为：18,Spike真的很帅

# s = "hello world"
# sio = io.StringIO(s)
# 等价于
sio = io.StringIO("hello world")
sio.seek(6)
sio.write("python")
print(sio.getvalue())  # hello python

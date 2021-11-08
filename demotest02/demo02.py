import turtle

for x in (1, 2, 3, 4):
    print(x ** 3)
for x in "spike":
    print(x)
di = {"name": "tom", "ege": 110, "job": "cat"}
for x in di:
    print(x)
for x in di.values():
    print(x)
for x in di.items():
    print(x)

print("_________________________________________________")
for x in range(1, 10):
    for y in range(1, x + 1):
        # print("{0}*{1}={2}".format(x, y, x * y))
        print(f'{x}*{y}={x * y}', end="\t")
    print()

print("--------------------------------------------------------")

var = [x ** 2 for x in range(1, 3)]
print(var)
print(sum(var))
s = 0
for x in range(0, len(var)):
    s += var[x]
print(s)
print("-------------------------------------------------------")

my_text = "hadoop,spark,yarn,mr"
text_count = {m: my_text.count(m) for m in my_text}
print(text_count)

text_count = {}
for m in my_text:
    text_count[m] = my_text.count(m)  # 键值对 m是键 text_count[m]是值
print(text_count)

for key in text_count:
    print(f"{key}出现{text_count[key]}次", end="\t")
print("--------------------------------------")
my_colors = ("red", "yellow", "blue", "black", "green")
t = turtle.Pen()
t.speed(10)
t.width(3)
for x in range(1, 10):
    t.color(my_colors[x % 5 - 1])
    t.circle(x * 20)
    t.penup()
    t.goto(0, -(x * 20))
    t.pendown()

turtle.done()

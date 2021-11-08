a = "ab_123"
b = "ab_123"
print(a is b)  # True

a1 = a + "ab_123"
a2 = "ab_123ab_123"

print(a1 is a2)  # False
print(a1 == a2)  # True

print(id(a1))
print(id(a2))

c = "ab#"
d = "ab#"
print(c is d)  # True

print("12" in a)  # True

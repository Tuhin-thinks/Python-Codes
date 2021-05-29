a = [42]
b = [a[0]+42] + a + [a.pop() % 4]
print(b)
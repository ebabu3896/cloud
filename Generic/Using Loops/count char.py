n = 1234
print(len(str(n)))

c = 0
while n > 0:
    n = n // 10
    c += 1
print(c)
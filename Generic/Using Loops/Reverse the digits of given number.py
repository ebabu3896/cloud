# Reverse the digits of given number

num = 1234
a = str(num)
print(a[::-1])

rev = 0
res = 0
while num >0:
    rev = num % 10
    res  = res*10 + rev
    num = num // 10
print(res)
import math
x = int(input("Enter the x value: "))
y = int(input("Enter the y value: "))
ab = 1
res= math.pow(x, y)
for i in range(1, y+1):
    ab *= x

def find_pow(N, pow):
    if pow==0:
        return 1

    return N * find_pow(N, pow-1) 

print(find_pow(x, y))

# print(x)
# print(ab)
# print(res)
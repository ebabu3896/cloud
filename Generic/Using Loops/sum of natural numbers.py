# Sum of natural numbers:

num = int(input("Enter the natural numbers: "))
#Using iterator
s = 0
while(num>0):
    s += num
    num -=1
print(s)

#using loops
num =5
k = 0
for i in range(1, num + 1):
    print(i)
    k += i
print(k)

# print(sum(range(1, num + 1)))
# Using recursion
num = 5
def find_sum(num):
    if num == 0:
        return 0
    return num + find_sum(num-1)

print(find_sum(num))
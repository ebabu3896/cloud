


num = 100
arr = []

#Using loops:
def find_prime(num):
    for i in range(1, num):
        flag = 0
        for n in range(2, i // 2 + 1):  # for n in range(2, int(num * 0.5)+1):
            if i % n == 0:
                flag = 1
                break
        if flag == 0:
            arr.append(i)
        flag = 0
find_prime(num)
print(arr)


#Using recursion:
arr1 = []
def find_prime_rec(num):
    for i in range(1, num):
        flag = 0
        n = 2
        while n < (i//2 +1):
            if i % n == 0:
                flag = 1
                break
            n += 1
        if flag == 0:
            arr1.append(i)
        flag = 0
find_prime_rec(num)
print(arr1)
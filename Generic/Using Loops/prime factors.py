
arr = []
def prime_factors(num):
    while num %2 == 0:
        arr.append(2)
        num = num//2
    
    for i in range(3, num//2 + 1,2):
        while num % i == 0:
            arr.append(i)
            num = num // i
    
    if num > 2:
        print(n)

num = 555
prime_factors(num)
print(arr)
#Fibonacci starting from any two number

num = int(input("Enter the value: "))

n1= 0 
n2 = 1
for i in range(2, num+1):
    n3 = n1 + n2
    n1 = n2
    n2 = n3

print(n3)

def fib(num, cache):
    if num <= 1:
        return num
    if num in cache:
        return cache[num]
    cache[num] = fib(num-1, cache) + fib(num-2, cache)
    return cache[num]

print(fib(num, {}))

def fib1(num):
    dp = [0, 1]
    if num<2:
        return dp[num]
    for i in range(2, num+1):
        n = dp[0] + dp[1]
        dp[0] = dp[1]
        dp[1] = n
    return dp[1]
print(fib1(num))
# Find the factors of a  number:

num = int(input("Enter the value: "))

arr = []
for i in range(2, num//2 + 1):
    if num % i == 0:
        arr.append(i)
print(arr)
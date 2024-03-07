# reverse array elements:

arr = [3,6,7,4,99,2,5,4]

# arr1 = []
# arr1 = arr[::-1]
# print(arr1)

# for i in range(len(arr) -1, -1, -1):
#     arr1.append(arr[i])
# print(arr1)

L = 0
R = len(arr) - 1
while L <= R:
    arr[L], arr[R] = arr[R], arr[L]
    L += 1
    R -= 1
print(arr)
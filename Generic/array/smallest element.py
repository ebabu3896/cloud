# Smallest among N numbers in an array
arr = [3,6,7,4,99,2,5,4]


# print(min(arr))
# arr.sort()
# print(arr[0])

val = arr[0]

if len(arr) == 1:
    print(arr[0])

for i in arr:
    if i < val:
        val = i
print(val)

val = min(arr, key = lambda x:x)
print(val)
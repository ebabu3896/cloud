# Largest among N numbers in an array

arr = [3,6,7,4,99,2,5,4]
# print(max(arr))
# arr.sort()
# print(arr[-1])
val  = arr[0]

# for i in arr:
#     if i > val:
#         val = i
# print(val)

val = max(arr, key = lambda x:x)
print(val)
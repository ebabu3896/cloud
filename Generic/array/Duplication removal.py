#Duplication removal

arr = [1,2,3,4,1,2]
# print(list(set(arr)))
print(arr)
# arr1 = []
# for i in arr:
#     if i not in arr1:
#         arr1.append(i)

# print(arr1)
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] in arr[i+1:]:
            arr.remove(arr[i])
print(arr)
#Palimdrome

num = 1221
num = str(num)
# temp = num
# rev = 0
# res = 0
# while num >0:
#     rev = num % 10
#     res  = res*10 + rev
#     num = num // 10
# print(res)
# if res == temp:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
L = 0
R = len(num) - 1
flag = 0
while L < R:
    if num[L] != num[R]:
        print("Not Palindomre")
        flag = 1
        break
    else:
        L += 1
        R -= 1
if flag == 0:
    print("Palimdrome")
#Palindrome checking
s = "malayalam"
flag = 0
L = 0
R = len(s) - 1
while L < R:
    if s[L] != s[R]:
        print("Not palindrome")
        flag = 1
    L += 1
    R -= 1
if flag == 0:
    print("Palindrome")
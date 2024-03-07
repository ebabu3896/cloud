#copying one string to another without using strcpy

s1 = "abcd"
s2 = "def"
# for i in s1:
#     s2 += i
# print(s2)

res = "".join((s1, s2))
print(res)
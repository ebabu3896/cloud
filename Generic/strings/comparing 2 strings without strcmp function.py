s1 = "abcd"
s2 = "a123"
import re
# if len(s1) != len(s2):
#     print("Not a match")

# for i in range(len(s1)):
#     if s1[i] != s2[i]:
#         print("Not a match")
#         break

pattern = re.compile(s2)
matc = re.search(pattern, s1)
if matc:
    print("match")
else:
    print("not match")
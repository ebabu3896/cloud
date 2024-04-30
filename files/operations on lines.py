'''File Handling Example 4'''

# import os
# file = open("C:/Users/Admin/Documents/ebabu/cloud/files/content.txt", 'r')
# print(file.readline())   #Reads single line.
# file.close()

# import os
# file = open("C:/Users/Admin/Documents/ebabu/cloud/files/content.txt", 'r')
# print(file.readlines())   #Reads all line.
# file.close()

import os
file = open("C:/Users/Admin/Documents/ebabu/cloud/files/content.txt", 'r')
for i in file:
    print(file.readline())   #loop all lines.
file.close()

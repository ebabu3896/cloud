import os
file = open("C:/Users/Admin/Documents/ebabu/cloud/files/wrtite_data.txt", 'w')
file.write("Hello world")   #write files
file.write("Welcome to python") 
file.close()

file = open("C:/Users/Admin/Documents/ebabu/cloud/files/wrtite_data.txt", 'r')
print(file.readlines())
file.close()

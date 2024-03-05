k = input("Enter the character: ")

if  97 <= ord(k) <= 123:
   print(chr(ord(k) - 32))
else:
   print("Entered is not a upper case char")
   print(k)

print(k.upper())
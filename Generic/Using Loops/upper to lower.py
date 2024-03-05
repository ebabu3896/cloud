k = input("Enter the character: ")

if  65 <= ord(k) <= 91:
   print(chr(ord(k) + 32))
else:
   print("Entered is not a upper case char")

print(k.lower())
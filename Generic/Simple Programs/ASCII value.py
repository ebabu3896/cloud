k = input("Enter the character: ")
class find_char:
    def __init__(self, k):
        self.k = k
    
    def char_value(self):
        res = ord(k)
        return res

ch = find_char(k)
print("Return value of char is: ",ch.char_value())

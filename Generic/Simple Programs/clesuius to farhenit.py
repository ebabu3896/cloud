cel = int(input("Enter the value: "))

class Cel:
    def __init__(self, cel):
        self.cel = cel
    
    def find_farhen(self):
        F = ((cel * 9/5) + 32)
        return F

cele = Cel(cel)
res = cele.find_farhen()
print("After conversation: ", res)

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
class rec:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def find_rectangle(self):
        AOE = self.l  * self.w
        return AOE

rectangle = rec(length, width)
res = rectangle.find_rectangle()
print("Rectangle area is :", res)
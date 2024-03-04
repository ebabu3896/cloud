val = int(input("Enter the value: "))
class find:
    def __init__(self, val):
        self.val = val
    def evenorodd(self):
        if self.val % 2 == 0:
            return "Even"
        else:
            return "Odd"
F1 = find(val)
res = F1.evenorodd()
print("Value is:", res)
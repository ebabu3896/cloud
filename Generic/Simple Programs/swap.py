val1 = int(input("Enter the first Value: "))
val2 = int(input("Enter the Second Value: "))

class Swap:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    def swap_values(self):
        self.val1, self.val2 = self.val2, self.val1
        return self.val1, self.val2
find = Swap(val1, val2)
res1, res2 = find.swap_values()
print("Values after swap: ", res1, res2)
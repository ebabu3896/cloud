val1 = int(input("Enter the input number: "))
val2 = int(input("Enter the input number: "))
val3 = int(input("Enter the input number: "))

class find_large:
    def __init__(self, val1, val2, val3):
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3
    
    def large_option1(self):
        if self.val1 > self.val2 and self.val1 > self.val3:
            return self.val1
        elif self.val2 > self.val1 and self.val2 > self.val3:
            return self.val2
        else:
            return self.val3
    
    def large_option2(self):
        return max(self.val1, self.val2, self.val3)
    
    def large_option3(self):
        maxV = self.val1 if self.val1 > self.val2 else self.val2
        maxV = maxV if maxV > self.val3 else self.val3
        return maxV

fl = find_large(val1, val2, val3)
#res = fl.large_option1()
#res = fl.large_option2()
res = fl.large_option3()
print("Largest among 3 numbers: ", res)
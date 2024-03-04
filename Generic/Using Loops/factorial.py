#Factorial of given number:
import math
class fact:
    def __init__(self, num):
        self.num = num
    
    def find_fact_recursive(self):
        num = self.num
        def find(num):
            if num <= 1:
                return 1
            return num * find(num - 1)
        return find(num)

    def find_fact_iterative(self):
        num = self.num
        temp = num
        if temp < 0:
            return 0
        elif temp == 0 or temp == 1:
            return 1
        else:
            fact = 1
            while (temp > 1):
                fact = fact*temp
                temp = temp - 1
            return fact
    
    def find_fact_func(self):
        num = self.num
        temp = 1
        for i in range(1, num+1):
            temp = temp* i
        return temp
    
    def find_fact_ternary(self):
        num = self.num
        def fact(num):
            return 1 if num == 0 or num == 1 else num*fact(num-1)
        return fact(num)
    
    def find_math(self):
        return math.factorial(self.num)
    
num = 5
ff = fact(num)
#print(ff.find_recursive())
#print(ff.find_fact_iterative())
#print(ff.find_fact_func())
# print(ff.find_fact_ternary())
print(ff.find_math())
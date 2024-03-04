val = input("Enter the char: ")
class find:
    def __init__(self, val):
        self.val = val
    def find_char(self):
        vow = set('aeiouAEIOU')
        if self.val in vow:
            return "Vowel"
        else:
            return "Consonant"
ch = find(val)
res = ch.find_char()
print("Given char is : ", res)
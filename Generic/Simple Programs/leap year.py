yearV = int(input("Enter the year: "))
import calendar
class find_year:
    def __init__(self, yearV):
        self.yearV = yearV
    
    def year_option1(self):
        if (self.yearV % 400 == 0) or (self.yearV % 4 ==0 and self.yearV % 100 != 0):
            return True
        else:
            return False
    
    # Using Calender option
    def year_option2(self):
        if calendar.isleap(self.yearV):
            return True
        else:
            return False

    # Using lambda option:
    def year_option3(self):
        res = lambda yearV: (self.yearV % 400 == 0) or (self.yearV % 4 ==0 and self.yearV % 100 != 0)
        return res


fy = find_year(yearV)
# res = fy.year_option1()
# res = fy.year_option1()
res = fy.year_option1()
if res == True:
    print("Entered year is leap year")
else:
    print("Entered year is not leap year")

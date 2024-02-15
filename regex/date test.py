import re
dates = '''
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''

#pattern = re.compile(r'\d\d\d\d.\d\d.\d\d')
#pattern1 = re.compile(r'\d\d\d\d-\d\d-\d\d')   #To access dates seperated by -
#pattern2 = re.compile(r'\d\d\d\d[-/]\d\d[-/]\d\d')  #To access dates seperated by either - or / 
#pattern3 = re.compile(r'\d\d\d\d[-/]0[56][-/]\d\d')  #to access dates on only may/june only
pattern4 = re.compile(r'\d{4}[-/]0[5-7][-/]\d{2}')  #use quantifiers
matches = re.finditer(pattern4, dates)
for mat in matches:
    print(mat)
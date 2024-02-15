import re
my_string = """
hello world
1233
2020-05-20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
"""

pattern = re.compile(r'Mr\s\w+')
pattern1 = re.compile(r'Mr\.\s\w+')
pattern2 = re.compile(r'Mr\.?\s\w+')
pattern3 = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+')
matches = re.finditer(pattern3, my_string)
for mat in matches:
    print(mat)
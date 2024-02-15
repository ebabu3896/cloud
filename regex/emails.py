import re

emails = """
hello world
1233
2020-05-20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""

pattern = re.compile(r'[a-zA-z0-9-]+@')
pattern1 = re.compile(r'[a-zA-z0-9-]+@[a-zA-Z-]+\.[a-z]+')
pattern2 = re.compile(r'[a-zA-z0-9-]+@[a-zA-Z-]+\.(com|de|org)')
pattern3 = re.compile(r'[a-zA-z0-9-]+@[a-zA-Z-]+\.[a-zA-Z]+')
pattern4 = re.compile(r'([a-zA-z0-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)')
matched = re.finditer(pattern4, emails)
for mat in matched:
   # print(mat.group(0)) 
    print(mat.group(1))
   #print(mat.group(2))
   #print(mat.group(3))
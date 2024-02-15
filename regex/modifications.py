import re
#Split, sub

# test_string = 'abc123ABCDEF123abc'

# pattern = re.compile(r"123")
# splitted = pattern.split(test_string)
# print(splitted)

#output : ['abc', 'ABCDEF', 'abc']

#Substituting with another string
# test_string = "hello world, you are the best world"
# pattern = re.compile(r"world")
# subbed_string = pattern.sub('planet', test_string)
# print(subbed_string)

urls = """
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""
pattern = re.compile(r"https?://(www\.)?([a-zA-Z-]+)\.([a-zA-Z]+)")
matches = pattern.finditer(urls)
for mat in matches:
    print(mat)

subbed_urls = pattern.sub(r"\2\3", urls)
print(subbed_urls)
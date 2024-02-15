#  https://www.youtube.com/watch?v=AEE9ecgLgdQ

import re

# test_string = '123abc456789abc123ABC'

# pattern = re.compile(r'abc')
# matches = pattern.finditer(test_string)

# matches = re.finditer(r"abc", test_string)  #r indicates raw string
# for match in matches:
#     print(match)

# a = '\tHello'
# print(a)

# a = r'\tHello'
# print(a)

#1 . Methods to search for matches
#There are 3 methods for finding the matches
# match()    search for matched string at starting of the string
# search()   scans through the string and return the first matching index position.
# findall()  search for all matching string in the entire string
#finditer()  return all matched index position in the given string.

#test_string = '123abc456789abc123ABC'

# pattern = re.compile(r'abc')
# matches = pattern.findall(test_string)

# for match in matches:
#     print(match)

#output:
    #abc
    #abc

# pattern = re.compile(r'abc')
# matches = pattern.match(test_string)    
# print(matches)

#output:
    # None  Since we are using string as "abc" which is not there in test_string

# match object

# test_string = '123abc456789abc123ABC'
# pattern = re.compile(r'123')
# matches = pattern.match(test_string)    
# print(matches)

#output: <re.Match object; span=(0, 3), match='123'>
#since it is matching string at starting positon it will return the index position.

# test_string = '123abc456789abc123ABC'
# pattern = re.compile(r'123')
# matches = pattern.search(test_string)    
# print(matches)

# test_string = '123abc456789abc123ABC'
# pattern = re.compile(r'abc')
# matches = pattern.finditer(test_string)
# for matching in matches:
#     print(matching)

# Output:
# <re.Match object; span=(3, 6), match='abc'>
# <re.Match object; span=(12, 15), match='abc'>
    
#2. Methods on a match Object
# Functions we can try on finditer function:
    #group
    #start To return starting pos of index
    #end   To return ending pos of index
    #span  To return only span of the index

# test_string = '123abc456789abc123ABC'
# pattern = re.compile(r'abc')
# matches = pattern.finditer(test_string)
# for matching in matches:
#     print(matching.span(), matching.start(), matching.end(), matching.group())

#ouput:
    #(3, 6) 3 6 abc
    #(12, 15) 12 15 abc

#3. Meta characters:
    # All meta characters: . ^ $ * + ? { } [ ] \ | ( )

#. will search for any character except new line

# test_string = '1aDb'
# pattern = re.compile(r'.')
# matches = pattern.finditer(test_string)
# for matching in matches:
#     print(matching.group(), end = ' ')

#output: 1 a D b 

# if you want to search actual "." then we can use as 
# test_string = '1aDb.'
# pattern = re.compile(r'\.')
# matches = pattern.finditer(test_string)
# for matching in matches:
#     print(matching)

#output: <re.Match object; span=(4, 5), match='.'>
    
# ^  uses for search the starting position of matched string.
# test_string = '123abc456789abc123ABC'
# pattern = re.compile(r'^123')
# matches = pattern.finditer(test_string)
# for matching in matches:
#     print(matching)

#output : <re.Match object; span=(0, 3), match='123'>

# $ use for finding the matching last char in the string
# test_string = '123abc456789abc123ABC'
# pattern = re.compile(r"ABC$")
# matches = re.finditer(pattern, test_string)
# for mat in matches:
#     print(mat)

#Output <re.Match object; span=(18, 21), match='ABC'>
    
# test_string = 'hello 123_ heyho hohey'
# pattern = re.compile(r"\d")
# matches = re.finditer(pattern, test_string)
# for mat in matches:
#     print(mat)

#output:
#<re.Match object; span=(6, 7), match='1'>
#<re.Match object; span=(7, 8), match='2'>
#<re.Match object; span=(8, 9), match='3'>

# test_string = 'hello 123_ heyho hohey'
# pattern = re.compile(r'\D')
# matches = re.finditer(pattern, test_string)
# for mat in matches:
#     print(mat.span(), end = "")

#ouput: (0, 1)(1, 2)(2, 3)(3, 4)(4, 5)(5, 6)(9, 10)(10, 11)(11, 12)(12, 13)
    #(13, 14)(14, 15)(15, 16)(16, 17)(17, 18)(18, 19)(19, 20)(20, 21)(21, 22)

# \s to pring wide space characters
# test_string = 'hello 123_ heyho hohey'
# pattern = re.compile(r'\s')
# matches = pattern.finditer(test_string)
# for mat in matches:
#     print(mat)

#Output:
    #<re.Match object; span=(5, 6), match=' '>
    #<re.Match object; span=(10, 11), match=' '>
    #<re.Match object; span=(16, 17), match=' '>

# test_string = 'hello 123_ heyho hohey'
# pattern = re.compile(r'\S')
# matches = pattern.finditer(test_string)
# for mat in matches:
#     print(mat.span(), end ="")

#output (0, 1)(1, 2)(2, 3)(3, 4)(4, 5)(6, 7)(7, 8)(8, 9)(9, 10)(11, 12)(12, 13)
    #(13, 14)(14, 15)(15, 16)(17, 18)(18, 19)(19, 20)(20, 21)(21, 22)

# test_string = 'hello 123_ heyho hohey'
# pattern = re.compile(r'\w')
# matches = pattern.finditer(test_string)
# for mat in matches:
#     print(mat.span(), end ="")

# output (0, 1)(1, 2)(2, 3)(3, 4)(4, 5)(6, 7)(7, 8)(8, 9)(9, 10)(11, 12)(12, 13)
    #(13, 14)(14, 15)(15, 16)(17, 18)(18, 19)(19, 20)(20, 21)(21, 22)

# test_string = 'hello 123_ heyho hohey'
# pattern = re.compile(r'\W')
# matches = pattern.finditer(test_string)
# for mat in matches:
#     print(mat.span(), end ="")

#output: (5, 6)(10, 11)(16, 17)

# To find the beginning/ after space of the string
# test_string = 'hello 123_ heyho hohey'
# pattern = re.compile(r'\bhello')
# matches = pattern.finditer(test_string)
# for mat in matches:
#     print(mat)

#output: <re.Match object; span=(0, 5), match='hello'>

# test_string = 'hello 123_ heyho hohey'
# pattern = re.compile(r'\bhey')
# matches = pattern.finditer(test_string)
# for mat in matches:
#     print(mat)

#output: <re.Match object; span=(11, 14), match='hey'>

# test_string = 'hello 123_ heyho hey'
# pattern = re.compile(r'\bhey')
# matches = pattern.finditer(test_string)
# for mat in matches:
#     print(mat)

#output
    #<re.Match object; span=(11, 14), match='hey'>
    #<re.Match object; span=(17, 20), match='hey'>

#print the data which is not at staring of the block

# test_string = 'hello 123_ heyho hohey'
# pattern = re.compile(r'\Bhey')
# matches = pattern.finditer(test_string)
# for mat in matches:
#     print(mat)

#output: <re.Match object; span=(19, 22), match='hey'>
#Adding test cases
#Sets:
# uses [] and useful for checking multiple characters
# test_string = "hello 123_"
# pattern = re.compile(r'[lo]')
# matches = re.finditer(pattern, test_string)
# for mat in matches:
#     print(mat)

#output  It will look for all char mentioned in []
#<re.Match object; span=(2, 3), match='l'>
#<re.Match object; span=(3, 4), match='l'>
#<re.Match object; span=(4, 5), match='o'>

# test_string = "hello 123_"
# pattern = re.compile(r'[a-z]')
# matches = re.finditer(pattern, test_string)
# for mat in matches:
#     print(mat)

#output
#<re.Match object; span=(0, 1), match='h'>
#<re.Match object; span=(1, 2), match='e'>
#<re.Match object; span=(2, 3), match='l'>
#<re.Match object; span=(3, 4), match='l'>
#<re.Match object; span=(4, 5), match='o'>
    
# test_string = "hello 123_"
# pattern = re.compile(r'[0-9]')
# matches = re.finditer(pattern, test_string)
# for mat in matches:
#     print(mat)

#output:
#<re.Match object; span=(6, 7), match='1'>
#<re.Match object; span=(7, 8), match='2'>
#<re.Match object; span=(8, 9), match='3'>

# test_string = "hello 123_"
# pattern = re.compile(r'[a-zA-Z0-9]')
# matches = re.finditer(pattern, test_string)
# for mat in matches:
#     print(mat)

#output
#<re.Match object; span=(0, 1), match='h'>
#<re.Match object; span=(1, 2), match='e'>
#<re.Match object; span=(2, 3), match='l'>
#<re.Match object; span=(3, 4), match='l'>
#<re.Match object; span=(4, 5), match='o'>
#<re.Match object; span=(6, 7), match='1'>
#<re.Match object; span=(7, 8), match='2'>
#<re.Match object; span=(8, 9), match='3'>
    
#Quantifer:
# test_string = "hello 123_"
# pattern = re.compile(r'\d+')
# matches = re.finditer(pattern, test_string)
# for mat in matches:
#     print(mat)

#output: <re.Match object; span=(6, 9), match='123'>

my_string = "Hello World"
pattern = re.compile(r"world", re.I)
matches = pattern.finditer(my_string)
for mat in matches:
    print(mat)
    
# test_string = "hello _123"
# pattern = re.compile(r'\{1,3}')
# matches = re.finditer(pattern, test_string)
# for mat in matches:
#     print(mat)


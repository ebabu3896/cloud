
#Ref: https://www.youtube.com/watch?v=bnSYeYFRCaA
#String Operations:

#1. captalize()
str = 'hello'
print(str.capitalize())

#output: Hello [Captailize first char]


#2. casefold()
text = 'MARIo'
text2 = 'maRIO'
print(text.casefold())
print(text2.casefold())

#output:
#mario
#mario  (Covert to easily comparible case)

#3: center()
text = 'Sarath'
print(text.center(20))
#output:        Sarath   
print(text.center(20, "."))
#output:.......Sarath.......

#4: count()
text = 'abc_abc_abc_abc'
print(text.count('ab'))
#output: 4

#5: encode()
text = 'Elon Musk'
print(text.encode(encoding='UTF-8', errors='strict'))
#output: b'Elon Musk'

#6: endswith()
text = 'apple'
print(text.endswith('e'))
#output: True

#We can give input in tuple format where it will apply or operation.
print(text.endswith(('e', 'a')))
#output: True

#7: expandtabs()
text = 'text1\ttext2\ttext3'
#Gets tab space of 10 
print(text.expandtabs(10))
#output: text1     text2     text3


#8 find()
text = 'Remember to comment and subscribe'

position = text.find('subscribe')
print(position)

#print(everythings after postion)
print(text[position:])
#output
# 24
# subscribe

position = text.find('abdhak')
print(position)
#output: -1


#9: format()
text = '{subject} is doing: {action}.'
print(text.format(subject='cat', action='meow'))
#output: cat is doing: meow.

text = '{} is doing: {}.'
print(text.format('cat', 'meow'))
#output: cat is doing: meow.

#10: format_map()
coordinates = {'x':10, 'y': -5}
text = 'Coordinates: ({x}, {y})'
print(text.format_map(coordinates))
#output: Coordinates: (10, -5)

#11: index()  Similar to find(), but if element not found it will return error
text =  "Astronauts recently discovered a banana on the moon?"

position = text.index('banana')
print(position)
print(text[position:])
#output:
#33
#banana on the moon?

position = text.index('a')
print(position)
print(text[position:])

#output  Gets an error 
#   File "c:\Users\Admin\Documents\ebabu\cloud\strings\string operations.py", line 95, in <module>
#     position = text.index('icaha')
#                ^^^^^^^^^^^^^^^^^^^
# ValueError: substring not found


#12. isalnum()
text = 'hellokitty123'
print(text.isalnum())
#output True

text = 'hellokitty!'
print(text.isalnum())
#output False

#13: isalpha()
text = 'hellokitty'
print(text.isalpha())
#output True

text = 'hellokitty123'
print(text.isalpha())
#output False


#14: isascci()
text = "Hello"
print(text.isascii())
#output: True

text = "Hello©"
print(text.isascii())
#output: False

#18 isidentifer()  #it will evaluate whether given is normal stirng or not.
text = 'test_sample'
print(text.isidentifier())
#output: True

text = 'test-sample'
print(text.isidentifier())
#output: False

text = '1test_sample'
print(text.isidentifier())
#output: False


#19. islower()
text = 'Abc'
print(text.islower())
#Output: False

text = 'abc'
print(text.islower())
#Output: True

#20: isprintable()
text = 'text'
print(text.isprintable())
#output: True

text = 'text\n'
print(text.isprintable())
#output: False

#21: isspace()
text = "   "
print(text.isspace())
#output: True

text = "abc  de"
print(text.isspace())
#output: False

#22. istitle()  Checks whether first char of every string in given word os captial or not.
text = 'The Video'
print(text.istitle())
#output: True

text = 'the video'
print(text.istitle())
#output: False

#23. isupper()
text = 'BANANAS'
print(text.isupper())
#output: True

#24. join()
text = '-'
print(text.join(['text1', 'text2', 'text3']))
#output: text1-text2-text3

print('-'.join(['text1', 'text2', 'text3']))
#output: text1-text2-text3

#25: ljust()
text = 'text'
print(text.ljust(20, '-'))
#output: text----------------

#26. rjust()
text = 'text'
print(text.rjust(20, '-'))
#Output: ----------------text

#27. lower()
text =  "UPPERCASE"
print(text.lower())
#Ouput: uppercase

#28. lstrip()
text = 'Some text.'
print(text.lstrip('Some'))
# Output:  text.

text = 'Some text.'
print(text.rstrip('Some'))
#output: Some text.


#29 maketrans() & translate()
text = 'That is Bacon Baby'
table = text.maketrans('B', '😉')

print(table)
print(text.translate(table))
#output:
# {66: 128521}
# That is 😉acon 😉aby


#30 partition()
text = 'a+b=c'
print(text.partition('='))
#Output: ('a+b', '=', 'c')


#31. removeprefix()
text = 'Wazzap'
print(text.removeprefix('Wazz'))
#Output ap


#32. removesuffix()
text = 'Mister Everyone'
print(text.removesuffix('one'))
#Output Mister Every


#33. replace()
text = 'Remember to comment'
print(text.replace('comment', 'Subscribe'))
#Output : Remember to Subscribe

text = 'Remember to comment & comment'
print(text.replace('comment', 'Subscribe', 1)) #1 specify how many times we need change
#Output : Remember to Subscribe & comment

#34. rfind()
text = 'A:Some text. A'
pos = text.rfind('A')
print(pos)
#output: 13

pos = text.find('A')
print(pos)
#output: 0

pos = text.rfind('jkdnkjsd')
print(pos)
#output: -1

#34. rindex()
text = 'A:Some text. A'
pos = text.rindex('A')
print(pos)
#output: 13

pos = text.index('A')
print(pos)
#output: 0

pos = text.rindex('A')
print(pos)
#output: Exception
#     pos = text.rindex('jkdnkjsd')
#           ^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: substring not found


#37: rpartition()
text = 'text=text2=text3'
print(text.rpartition('=')) #partation will happen in reverse order
#output: ('text=text2', '=', 'text3')


#38: rsplit()
text = 'This is some special stuff'
print(text.rsplit(' '))
#output: ['This', 'is', 'some', 'special', 'stuff']

print(text.rsplit(sep = ' '))
#output: ['This', 'is', 'some', 'special', 'stuff']

text = 'This is some special stuff'
print(text.split(maxsplit=2))
#output: ['This', 'is', 'some special stuff']

#39. split()
text = 'www.website.com'
print(text.split(sep='.'))
#output: ['www', 'website', 'com']

print(text.split('.'))
#output: ['www', 'website', 'com']


#40: rstrip()
text = "He is my mario, mario"
print(text.rstrip('mario'))
#output: He is my mario,


#41: splitlines()
text = 'Remember to comment!\nor else... \n'
print(text.splitlines())
#output: ['Remember to comment!', 'or else... ']


#42: startswith()
text = 'Sarath'
print(text.startswith('S'))
#Output: True

print(text.startswith('a'))
#Output: False


#43.strip() #works only for first or last words
text = 'Sarath has pasta.'
print(text.strip('Sarath'))
#Output: has pasta.

print(text.strip('pasta.'))
#Output: 'Sarath has'

print(text.strip('has'))
#output: 'Sarath has pasta.'


#44. swapcase()
text = 'Sarath has pasta'
print(text.swapcase())
#Output: "sARATH HAS PASTA"


#45. title()
text = 'title is a title'
print(text.title())
#Output: 'Title Is A Title'


#46. upper()
text = 'hello there!'
print(text.upper())
#Output: HELLO THERE!


#47. zfill()
text = 'text'
print(text.zfill(20))
#Output: 0000000000000000text



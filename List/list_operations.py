#1: append()
people = ['abc', 'def', 'chi']

people.append('xyz')
print(people)
#output: ['abc', 'def', 'chi', 'xyz']

#2.clear() #empty the list
people = ['abc', 'def', 'chi']

people.clear()
print(people)
#output: []


#3. copy()
people = ['Mario', 'Elon', 'Trump']
copy_people = people.copy()
copy_people.remove('Mario')
print(people)
print(copy_people)
#Output:
#['Mario', 'Elon', 'Trump']
#['Elon', 'Trump']


#4. count()
people = ['Mario', 'Elon', 'Trump', 'Elon']
elons = people.count('Elon')
print(elons)
#Output: 2


#5. extend()
people = ['Mario', 'Elon', 'Trump']
people2 = ['Apple', 'Bannana']
people.extend(people2)
print(people)
#Output: ['Mario', 'Elon', 'Trump', 'Apple', 'Bannana']


#6.index()
people = ['Mario', 'Elon', 'Trump']
print(people.index('Trump'))
#output: 2


#7. insert()
people = ['Mario', 'Elon', 'Trump']
people.insert(2, 'babu')
print(people)
#Output: ['Mario', 'Elon', 'babu', 'Trump']

#8.pop()
people = ['Mario', 'Elon', 'babu', 'Trump']
people.pop()
print(people)
#Output: ['Mario', 'Elon', 'babu'] #last element

people.pop(1) #using index
print(people)
#Output: ['Mario', 'babu'] #index valued element removed


#9. remove()
people = ['Mario', 'Elon', 'babu', 'Trump']
people.remove('Elon')
print(people)
#Output: ['Mario', 'babu', 'Trump']
#If you give element not in list we will get exception.


#10. reverse()
people = ['Mario', 'Elon', 'babu', 'Trump']
people.reverse()
print(people)
#Ouput: ['Trump', 'babu', 'Elon', 'Mario']


#11. sort()
people = ['mario', 'elon', 'babu', 'trump']
people.sort()
print(people)
#output: ['babu', 'elon', 'mario', 'trump']

people = ['mario', 'elon', 'babuuuu', 'trump']
people.sort(key=lambda name:len(name))
print(people)
#Output: ['elon', 'mario', 'trump', 'babuuuu']

people = ['mario', 'elon', 'babuuuu', 'trump']
people.sort(key=lambda name:len(name), reverse=True)
print(people)
#Output: ['babuuuu', 'mario', 'trump', 'elon']
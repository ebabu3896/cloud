
#1 - values()
users = {0 : 'Mario', 1 : 'Luigi', 2: 'James'}
print(users.values())
#Output: dict_values(['Mario', 'Luigi', 'James'])


#2 - keys()
users = {0 : 'Mario', 1 : 'Luigi', 2: 'James'}
print(users.keys())
#Output: dict_keys([0, 1, 2])


#3 - pop() #removed specfic key element
users = {0 : 'Mario', 1 : 'Luigi', 2: 'James'}
users.pop(2)
print(users)
# Output: {0: 'Mario', 1: 'Luigi'}
#If you try to remove key which is not exist in dict then we will get error.


#4 - popitem() #removes last element from list
users = {0 : 'Mario', 1 : 'Luigi', 2: 'James'}
users.popitem()
print(users)
# Output: {0: 'Mario', 1: 'Luigi'}


#5-copy()
sample_dict = {0: ['a', 'b'], 1: ['c', 'd']}
my_copy = sample_dict.copy()
print(sample_dict)
print(my_copy)

#Output:
#{0: ['a', 'b'], 1: ['c', 'd']}
#{0: ['a', 'b'], 1: ['c', 'd']}

#By default it is shallow copy, if we change anything it will reflect original also
my_copy[0][0] = '!!!'
print(sample_dict)
print(my_copy)
#Output:
#{0: ['!!!', 'b'], 1: ['c', 'd']}
#{0: ['!!!', 'b'], 1: ['c', 'd']}


#6 -get()
users = {0 : 'Mario', 1 : 'Luigi', 2: 'James'}
#print(users.get(key, 'value to give if key is not there'))
print(users.get(1, 0))
print(users.get(100, 'Missing'))
#Output:
# Luigi
# Missing


#7. setdefault()
users = {0 : 'Mario', 1 : 'Luigi', 2: 'James'}
print(users.setdefault(0, '???'))
print(users.setdefault(999, '????'))
#Output:
#Mario
#????


#8. - clear()
users = {0 : 'Mario', 1 : 'Luigi', 2: 'James'}
users.clear()
print(users)
#Output: {}


#9 - from keys()
people = ['Mario', 'james', 'jackson']
users = dict.fromkeys(people)
print(users)
#Output:  {'Mario': None, 'james': None, 'jackson': None}


#10 - items()
users = {0 : 'Mario', 1 : 'Luigi', 2: 'James'}
print(users.items())
#Output: dict_items([(0, 'Mario'), (1, 'Luigi'), (2, 'James')])

for k , v in users.items():
    print(k, v)
#Output:
#0 Mario
#1 Luigi
#2 James


#11. update()
users =  {0 : 'Mario', 1 : 'Luigi', 2: 'James'}
users.update({2 : 'raju', 3: 'bala'})
print(users)
#Output: {0: 'Mario', 1: 'Luigi', 2: 'raju', 3: 'bala'}

user2 = {5: 'bsakdhb', 6:'uhlow'}
users.update(user2)
print(users)
#Ouptut: {0: 'Mario', 1: 'Luigi', 2: 'raju', 3: 'bala', 5: 'bsakdhb', 6: 'uhlow'}

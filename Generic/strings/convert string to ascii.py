#  Convert String list to ascii values

test_list = ['gfg', 'is', 'best']

res = []
for item in test_list:
    for val in item:
        res.append(ord(val))

print(res)
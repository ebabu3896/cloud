# Multiplication table

num = int(input("Enter the table you want: "))

# for i in range(1, 11):
#     print(num, "*", i, "=", num*i)

print('\n'.join([f"{num} * {i} = {num*i}" for i in range(1, 11)]))
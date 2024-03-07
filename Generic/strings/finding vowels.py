
vowels = set("aeiouAEIOU")
st = "nalkdnkdjaaaaiiiiaaaancvklandv"
count = 0
for s in st:
    if s in vowels:
        count += 1
print(count)
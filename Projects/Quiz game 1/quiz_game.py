print("Welcome to my computer quiz!")


playing = input("Do you want to play? ")
print(playing)

if playing != ("yes" or "YES"):
    quit()

print("OK! Let's Play")

ans = input("What does CPU stands for? ")
if ans ==  "Central Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")

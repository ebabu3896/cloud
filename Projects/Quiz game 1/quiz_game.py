print("Welcome to my computer quiz!")


playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("OK! Let's Play")
score  =0
ans = input("What does CPU stands for? ")
if ans.lower() ==  "central processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

ans = input("What does GPU stands for? ")
if ans.lower() ==  "graphics processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

ans = input("What does RAM stands for? ")
if ans.lower() ==  "random access memory":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

print(f"Score is {score}")
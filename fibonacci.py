from random import randint

print("Welcome to Piglet!")
x="y"
roll=0
total=0
while x!="n" and roll!=1:
    roll=randint(1,6)
    print("You rolled a",roll)
    total+=roll
    if roll==1:
        total=0
        print("You got",total,"points.")
        break
    x=input("Roll again? ").lower()
    if x=="n" or x=="no":
        print("You got", total, "points.")
        break
    else:
        continue


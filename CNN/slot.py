import random

list_1 = ["🎈","🎉","🎁","🍕","⚠️ ","💲"]
list_2 = ["🎈","🎉","🎁","🍕","⚠️ ","💲"]
list_3 = ["🎈","🎉","🎁","🍕","⚠️ ","💲"]

random.shuffle(list_1)
random.shuffle(list_2)
random.shuffle(list_3)
count = int(input("Please give a number: "))
for x in range(count):
    x1 = random.choice(list_1)
    x2 = random.choice(list_2)
    x3 = random.choice(list_3)
    print(x1,x2,x3)
    if x1 == x2 == x3:
        print("you win 😇 😉 😃 😀",x)
        exit(0)

print("You are loser !")

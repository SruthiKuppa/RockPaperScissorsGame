import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice=[]
total=0
#number of dice you like to roll:
numOfDice=int(input("How many dice? :"))

for die in range(numOfDice):
    dice.append((random.randint(1,6)))

#to print the lines of each dice from the diceart sequentially:
#for die in range(numOfDice):
#    for line in dice_art.get(dice[die]):
#        print(line)

#to print the dice adjacent to each other:
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end="")
    print()
#to display the sum of random number rolled by algo
for die in dice:
    total+=die
print(f"total:{total}")

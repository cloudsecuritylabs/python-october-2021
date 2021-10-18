# convert this to a function
# create a module and call it.
from random import randrange

dice = { 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

print(type(dice))

dice_roll = int(input("Times to roll the dice? "))
print("Rolling the dice ...")

for i in range(dice_roll):
    dice_roll_val = randrange(1, 7) # why?
    dice[dice_roll_val] = dice[dice_roll_val] + 1

print(dice)
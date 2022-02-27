from random import randrange
def main():
    dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    dice_roll_result(dice)
def dice_rolling():
    dice_roll = int(input("Times to roll the dice: "))
    print(dice_roll)
    return dice_roll
def dice_roll_result(dice):
    for i in range(dice_rolling()):
        dice_num = randrange(1,7)
        dice[dice_num] = dice[dice_num] + 1
    print(dice)
main()
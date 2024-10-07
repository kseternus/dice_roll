import random

dice_sides = [1, 2, 3, 4, 5, 6]
dice_ascii = [
    '┌─────────┐\n'
    '│         │\n'
    '│    ●    │\n'
    '│         │\n'
    '└─────────┘\n',

    '┌─────────┐\n'
    '│  ●      │\n'
    '│         │\n'
    '│      ●  │\n'
    '└─────────┘\n',

    '┌─────────┐\n'
    '│  ●      │\n'
    '│    ●    │\n'
    '│      ●  │\n'
    '└─────────┘\n',

    '┌─────────┐\n'
    '│  ●   ●  │\n'
    '│         │\n'
    '│  ●   ●  │\n'
    '└─────────┘\n',

    '┌─────────┐\n'
    '│  ●   ●  │\n'
    '│    ●    │\n'
    '│  ●   ●  │\n'
    '└─────────┘\n',

    '┌─────────┐\n'
    '│  ●   ●  │\n'
    '│  ●   ●  │\n'
    '│  ●   ●  │\n'
    '└─────────┘\n'
]


def diceRoll(dices):
    print('Rolled dices: ')
    for i in range(dices):
        n = random.choice(dice_sides) - 1
        print(f'Dice no. {i+1}: rolled out {dice_sides[n]}')
        print(f'{dice_ascii[n]}')


how_dices = int(input('How many dices to roll? '))
diceRoll(how_dices)

while True:
    roll_again = input('Roll again(Y/N)? ').upper()
    if roll_again == 'Y':
        how_dices = int(input('How many dices to roll this time? '))
        diceRoll(how_dices)
    elif roll_again == 'N':
        print('Good luck next time!\nBYE!')
        break

import random


class DiceRoller:
    """A class to simulate rolling dice with customizable sides and show dice results as ASCII art."""

    def __init__(self, sides=6):
        """Initialize the DiceRoller with a default of 6 sies."""
        self.sides = sides
        # ASCII art for dice faces 1-6
        self.dice_faces = {
            1: (
                '┌─────────┐\n'
                '│         │\n'
                '│    ●    │\n'
                '│         │\n'
                '└─────────┘\n'
            ),
            2: (
                '┌─────────┐\n'
                '│  ●      │\n'
                '│         │\n'
                '│      ●  │\n'
                '└─────────┘\n'
            ),
            3: (
                '┌─────────┐\n'
                '│  ●      │\n'
                '│    ●    │\n'
                '│      ●  │\n'
                '└─────────┘\n'
            ),
            4: (
                '┌─────────┐\n'
                '│  ●   ●  │\n'
                '│         │\n'
                '│  ●   ●  │\n'
                '└─────────┘\n'
            ),
            5: (
                '┌─────────┐\n'
                '│  ●   ●  │\n'
                '│    ●    │\n'
                '│  ●   ●  │\n'
                '└─────────┘\n'
            ),
            6: (
                '┌─────────┐\n'
                '│  ●   ●  │\n'
                '│  ●   ●  │\n'
                '│  ●   ●  │\n'
                '└─────────┘\n'
            ),
        }

    def roll(self):
        """Simulates rolling a dice with the given number of sides."""
        return random.randint(1, self.sides)

    def roll_multiple(self, number_of_dice=1):
        """Rolls multiple dice and returns the results."""
        return [self.roll() for _ in range(number_of_dice)]

    def get_dice_ascii(self, value):
        """Returns the ASCII art for the given dice value."""
        return self.dice_faces.get(value, 'Invalid dice value.')

    def display_rolls(self, number_of_dice=1):
        """Rolls multiple dice, displays the results, and prints the ASCII art for each dice."""
        rolls = self.roll_multiple(number_of_dice)
        print(f'Rolling {number_of_dice} dice: {rolls}')
        for roll in rolls:
            print(self.get_dice_ascii(roll))


# Example usage:
if __name__ == '__main__':
    on = True
    while on:
        user_input = input('How many dices to roll (1-10)?\nType "exit" to quit: ').strip().lower()

        if user_input == 'exit':
            on = False
            print('Exiting program.')
        else:
            try:
                how_many = int(user_input)
                if how_many in range(1, 11):
                    dice = DiceRoller(sides=6)  # Create a dice roller with 6 sides
                    dice.display_rolls(how_many)  # Roll dice and display results
                else:
                    print('Wrong amount, please select 1-10')
            except ValueError:
                print('Invalid input. Please enter an integer.')

# loop
# Ask user to roll the dice?.lower is to convert user choice in lower case..
#  If user enter y?
#   generate 2 random numbers
#   and print.
# If user enter n?
#  print thank You message
#  terminate
# else
#  print invalid choice

import random 

  
while True:
    choice = input("Roll the Dice? (y/n): ").lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif choice == 'n':
        print("Thanks for playing")
        break
    else:
        print("INVALID CHOICE")

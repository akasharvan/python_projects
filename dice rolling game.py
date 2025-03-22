import random 

# loop  
while True:
    # Ask user to roll the dice?.lower is to convert user choice in lower case.
    choice = input("Roll the Dice? (y/n): ").lower()
    #  If user enter y?
    if choice == 'y':
        #   generate 2 random numbers
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        #   and print.
        print(f'({die1},{die2})')
    # If user enter n?
    elif choice == 'n':
        #  print thank You message
        print("Thanks for playing")
        #  terminate
        break
    # else
    else:
        #  print invalid choice
        print("INVALID CHOICE")

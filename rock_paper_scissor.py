import random

# tupl
choices = ('r','p','s')

# loop
while True:
    # ask user to make a choice
    user_choice = input('Rock,paper or scissor(r/p/s): ').lower()
    # if the choice is not a valid
    if user_choice not in choices:
        #  print an error
        print('Invalid choice!')
        continue
    # let computer make a choice
    computer_choice = random.choice(choices)
    # print choice
    print(f'You chose {user_choice}')
    print(f'computer chose {computer_choice}')

    # determine the winner
    if user_choice == computer_choice:
        print('Tie')
    elif((user_choice == 'r' and computer_choice =='s') or
    (user_choice == 's' and computer_choice == 'p') or 
    (user_choice == 'p'and computer_choice =='r')):
        print('You Win')
    else:
        print('You lose')

    # ask the user if they want to continue
    should_continue =input('Continue? (y/n): ').lower()
    # if not 
    if (should_continue == 'n'):
        #  terminate
        break 






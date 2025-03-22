# ask user to make a choice
# if the choice is not a valid
#  print an error
# let computer make a choice
# print choice (emojis)
# determine the winner
# ask the user if they want to continue
# if not 
#  terminate


# import random

# # tupl
# choices = ('r','p','s')

# while True:
#     user_choice = input('Rock,paper or scissor(r/p/s): ').lower()
#     if user_choice not in choices:
#         print('Invalid choice!')
#         continue

#     computer_choice = random.choice(choices)
#     print(f'You chose {user_choice}')
#     print(f'computer chose {computer_choice}')

#     if user_choice == computer_choice:
#         print('Tie')
#     elif((user_choice == 'r' and computer_choice =='s') or
#     (user_choice == 's' and computer_choice == 'p') or 
#     (user_choice == 'p'and computer_choice =='r')):
#         print('You Win')
#     else:
#         print('You lose')

#     should_continue =input('Continue? (y/n): ').lower()
#     if (should_continue == 'n'):
#         break 

#    Modularization(smaller the code)

import random

# tupl
choices = ('r','p','s')

# function
def get_user_choice():
    while True:
        user_choice = input('Rock,paper or scissor(r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')

def display_choices(user_choice ,computer_choice):
    print(f'You chose {user_choice}')
    print(f'computer chose {computer_choice}')

def determine_winner(user_choice ,computer_choice ):
    if user_choice == computer_choice:
        print('Tie')
    elif((user_choice == 'r' and computer_choice =='s') or
    (user_choice == 's' and computer_choice == 'p') or 
    (user_choice == 'p'and computer_choice =='r')):
        print('You Win')
    else:
        print('You lose')  

def play_game(): 
    while True:

        user_choice = get_user_choice()
    
        computer_choice = random.choice(choices)

        display_choices(user_choice ,computer_choice)

        determine_winner(user_choice ,computer_choice)

        should_continue =input('Continue? (y/n): ').lower()
        if (should_continue == 'n'):
            break 

play_game()




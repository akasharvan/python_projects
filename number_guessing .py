# Generate a random number
# loop
    # Ask user to make a guess?
    # if not a valid number 
    #   Print an error
    # if number < guess
    #  print too low
    # If number > gusee
    #  print too high
    # else
    #  print well done



import random

num_to_guess = random.randint(1,100)
while True:
    try:
        guess = int(input('Guess the number b/w (1 to 100): '))
        if (guess < num_to_guess):
            print('your guess is too low')
        elif(guess > num_to_guess):
            print('your guess is too High')
        else:
            print ('congratulations! You guess the number')
            break
    except ValueError:
        print('Please enter a valid number')


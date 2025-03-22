import random

# Generate a random number
num_to_guess = random.randint(1,100)
# loop
while True:
    try:
        # Ask user to make a guess?
        guess = int(input('Guess the number b/w (1 to 100): '))
        # if number < guess
        if (guess < num_to_guess):
            #  print too low
            print('your guess is too low')
        # If number > gusee
        elif(guess > num_to_guess):
            #  print too high
            print('your guess is too High')
        # else
        else:
            #  print well done
            print ('congratulations! You guess the number')
            break
    except ValueError:
        #   Print an error
        print('Please enter a valid number')


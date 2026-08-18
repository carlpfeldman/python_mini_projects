#this is a guess the number game
import random
secret_number = random.randint(1,20)
print('I am thinking of a random number between 1 and 20')

#ask the player to guess six times
for guesses_taken in range(1,7):
    print('Take a guess: ')
    guess = int(input('>'))

    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('Your guess is too high')
    else:
        break #this condition is the correct guess!

if guess == secret_number:
    print('You guessed it in ' + str(guesses_taken) + ' guesses')
else:
    print('Nope, the number was ' + str(secret_number))



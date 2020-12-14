import random

guess = 0
tries = 0
value = random.randint(1, 10)
#print(value)            # debug code

print('Guess an number between 1 and 10\n')

while guess != value:
    tries += 1
    guess = input(f'Enter guess #{tries}: ')

    if guess.isnumeric():
        guess = int(guess)
    else:
        print('Numbers only, please!')
        continue

    if guess > value:
        print('Your guess is to high, try again!')
    elif guess < value:
        print('You guess is to low, try again!')    

else:
    print(f'You guessed it in {tries}!')
import random

guess = 0
tries = 0
value = random.randint(1, 10)
print(value)                    # debug code

print('Guess an number between 1 and 10\n')

while guess != value:
    tries += 1
    guess = input(f'Enter guess #{tries}: ')

    if guess.isnumeric():
        guess = int(guess)
        continue
    else:
        print('Numbers only, please!')
else:
    print(f'You guessed it in {tries}!')
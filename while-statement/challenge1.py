import random

guess = 0
tries = 0
actual = random.randint(1, 5)
# print(actual)

while guess != actual:
    guess = input('Guess an number between 1 and 5: ')
    tries += 1

    if guess.isnumeric():
        guess = int(guess)
        continue

print(f'You guessed it in {tries}!')

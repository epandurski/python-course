import random
import sys

def gen_rand_number():
    """Generates a 4-digit string."""
    
    numbers = [str(x) for x in range(10)]
    generated_numbers = []
    for x in range(4):
        n = random.choice(numbers)
        numbers.remove(n)
        generated_numbers.append(n)
    generated_number = ''.join(generated_numbers)
    if generated_number[0] == '0':
        return gen_rand_number()
    return generated_number

def match_numbers(secret, guess):
    assert len(secret) == len(guess) == 4
    bulls = 0
    cows = 0
    for i in range(4):
        n = guess[i]
        try:
            index_in_secret = secret.index(n)
        except ValueError:
            continue
        if  i == index_in_secret:
            bulls += 1
        else:
            cows += 1
    return bulls, cows


def get_user_guess():
    while True:
        s = input('Enter a 4-digit number: ')
        if s == 'exit':
            sys.exit()
        if len(s) == 4 and all([(x in '1234567890') for x in s]):
            break
        print('This is not a 4-digit number. Try again.')
    return s

    
random_secret = gen_rand_number()
n = 0
while True:
    user_guess = get_user_guess()
    n += 1
    bulls, cows = match_numbers(random_secret, user_guess)
    if bulls == 4:
        print('Correct! It took you {n} guesses.')
        break
    print(f'{bulls} bulls and {cows} cows. Try again.')

    
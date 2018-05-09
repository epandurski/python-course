DEVILS_NUMBER = 666


def _show_devils_number():
    print("The devil's number is", DEVILS_NUMBER)


def get_integer(prompt='Enter a number: '):
    return int(input(prompt))


def ask_for_devils_number():
    n = get_integer("What is the devil's number? ")
    if n != DEVILS_NUMBER:
        _show_devils_number()
    else:
        print('Correct!')

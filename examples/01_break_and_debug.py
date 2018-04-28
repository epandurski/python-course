# Пита за име, след което казва дали името съдържа латинската буква 'a'.

name = input('Enter a name: ')
i = 0
n = len(name)
while i < n:
    letter = name[i]
    if letter == 'a':
        print('The name contains "a".')
        break
    i = i + 1
else:
    print('The name does not contain "a".')

print('Thank you for using this program.')

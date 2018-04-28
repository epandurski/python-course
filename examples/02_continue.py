# Извежда числата от 2 до 9, казвайки ако числото е четно.

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

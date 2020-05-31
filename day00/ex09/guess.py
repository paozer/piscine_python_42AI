from random import randint

secret = randint(1, 99)
count = 0
user_input = input('Welcome! Enter your guess or exit ')

while user_input != 'exit':
    count += 1
    try:
        guess = int(user_input)
    except ValueError:
        user_input = input('This is not a number. Try again ')
        continue
    if guess > secret:
        user_input = input('Too high. Try again ')
    elif guess < secret:
        user_input = input('Too low. Try again ')
    else:
        print('Congratulations!')
        break

print(f'You had {count} tries!')

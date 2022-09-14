secret_number = 97
epsilon = 0.01
x = 100
low_num = 0
high_num = x
guess = int((high_num-low_num)/2)


print('Please think of a number between 0 and 100!')

while abs(guess-secret_number) >= epsilon:
    print('Is your secret number' +' '+ str(guess) +'?')
    r = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly. ')
    if r in ['l']:
        low_num = guess
        guess = int((high_num+low_num)/2)
    elif r in ['h']:
        high_num=guess
        guess = int((high_num+low_num)/2)
    elif r in ['c']:
        break
    else:
        print('Sorry, I did not understand your input.')

while guess == secret_number:
    print('Is your secret number' +' '+ str(guess) +'?')
    r = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly. ')
    if r in ['c']:
        break
    else:
        print('Sorry, I did not understand your input.')

print('Game over. Your secret number was: ' + str(guess))

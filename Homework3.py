import random


def Viselitsa(Word):
    print('VREMYA IGRAT VISELITSA')


dictionary = ['osyol', 'eshek', 'mango', 'kymyz', 'moloko', 'chipsy']
secret = random.choice(dictionary)
guesses = 'aeiou'
popytki = 5

while popytki > 0:
    missed = 0
    for letter in secret:
        if letter in guesses:
            print(letter, end=' ')

        else:
            print('_', end=' ')
            missed = missed + 1

    print()

    if missed == 0:
        print('\nYou win, KRASAVCHIK!')
        break

    guess = input('\nguess a letter: ')
    guesses += guess

    if guess not in secret:
        popytki = popytki - 1
        print('\nNope.')
        print('\n', popytki, 'more popytok')
        if popytki < 5: print('\n  |  ')
        if popytki < 4: print('  O  ')
        if popytki < 3: print(' /|\ ')
        if popytki < 2: print('  |  ')
        if popytki < 1: print(' / \ ')
        if popytki == 0:
            print('\n\nThe answer is', secret)

yesOrNo = ' yes'
while yesOrNo == ' yes':
    # Viselitsa()
    yesOrNo = input('Do you want play again? (yes or no)')
    if yesOrNo != "no":
        continue
    elif yesOrNo == "yes":
        break

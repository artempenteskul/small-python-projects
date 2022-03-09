import random


NUM_DIGITS = 3
NUM_MAX_GUESSES = 8


def getSecretNum():
    numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(numList)
    secretNum = ''.join(numList[:NUM_DIGITS])

    while secretNum.startswith('0'):
        random.shuffle(numList)
        secretNum = ''.join(numList[:NUM_DIGITS])

    return secretNum


def getClues(guess, secret):
    if guess == secret:
        return 'You got it. Well played!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clues.append('Fermi')
        elif guess[i] in secret:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


def main():
    print(
        f'''
            Bagels, a deductive logic game.
            I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
            
            Try to guess what it is. Here are some clues:
            When I say:      That means:
            Pico             One digit is correct but in the wrong position.
            Fermi            One digit is correct and in the right position.
            Bagels           No digit is correct.
             
            For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
        '''
    )

    while True:
        secretNum = getSecretNum()

        print('I have thought up a number.')
        print(f'You have {NUM_MAX_GUESSES} guesses to get it.')

        numGuesses = 1
        while numGuesses <= NUM_MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}:')
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > NUM_MAX_GUESSES:
                print('You are run out of guesses!')
                print(f'The answer was: {secretNum}.')

        print('Do you want to play again? (yes or no): ')
        if input('> ').lower().startswith('n'):
            break
    print('Thanks for the game!')


if __name__ == '__main__':
    main()

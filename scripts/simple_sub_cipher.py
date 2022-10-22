import sys
import random
import pyperclip


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('Simple Substitution Cipher!')
    print('A Simple Sub Cipher has a one-to-one translation for each symbol in the plaintext and each symbol in the ciphertext.')
    print()

    while True:
        print('Do you wanna (e)ncrypt or d(ecrypt) message? ')
        response = input('> ').lower()
        if response.startswith('e'):
            mode = 'encrypt'
            break
        elif response.startswith('d'):
            mode = 'decrypt'
            break

        print('Please enter e or d letter.')

    while True:
        print('Please specify the key to use.', end=' ')
        if mode == 'encrypt':
            print('Or enter RANDOM to get already generated key.')

        response = input('> ').upper()
        if response == 'RANDOM':
            key = generate_random_key()
            print(f'Your secret key to decrypt the message is: {key}')
            break
        else:
            if check_key(response):
                key = response
                break

    print(f'Enter message to {mode}: ')
    message = input('> ')

    if mode == 'encrypt':
        translated = encrypt_message(message, key)
    elif mode == 'decrypt':
        translated = decrypt_message(message, key)
    else:
        raise Exception

    print()
    print(f'The {mode}ed message is: ')
    print(f'{translated}')

    try:
        pyperclip.copy(translated)
    except Exception as e:
        print(f'An error while copying message to clipboard: {e}')
        pass
    else:
        print()
        print('Message copied to clipboard!')
        sys.exit()


if __name__ == '__main__':
    main()

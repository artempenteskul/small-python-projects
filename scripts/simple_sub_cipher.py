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


def check_key(key):
    key_list = list(key)
    letters_list = list(LETTERS)
    key_list.sort()
    letters_list.sort()
    if key_list != letters_list:
        print('There is an error in the key or symbol set. Try another key.')
        return False
    return True


def encrypt_message(message, key):
    return translate_message(message, key, mode='encrypt')


def decrypt_message(message, key):
    return translate_message(message, key, mode='decrypt')


def translate_message(message, key, mode):
    translated = ''
    normal_letters_order = LETTERS
    key_letters_order = key

    if mode == 'decrypt':
        normal_letters_order, key_letters_order = key_letters_order, normal_letters_order

    for char in message:
        if char.upper() in normal_letters_order:
            char_index = normal_letters_order.find(char.upper())
            if char.isupper():
                translated += key_letters_order[char_index].upper()
            else:
                translated += key_letters_order[char_index].lower()
        else:
            translated += char

    return translated


def generate_random_key():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()

import pyperclip


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('The Viginere Cipher Script!')
    print('The Vigenere Cipher is a polyalphabetic substitution cipher that was powerful enough to remain unbroken for centuries.')
    print()

    while True:
        print('Do you want to e(ncrypt) or d(ecrypt)?')
        response = input('> ').lower()
        if response.startswith('e'):
            mode = 'encrypt'
            break
        elif response.startswith('d'):
            mode = 'decrypt'
            break
        print('Please enter "e" or "d" letter.')

    while True:
        print()
        print('Please specify the key to use.')
        print('It can be a word or any combination of letters.')
        response = input('> ').upper()
        if response.isalpha():
            key = response
            break

    print()
    print(f'Enter the message to {mode}: ')
    message = input('> ')

    if mode == 'encrypt':
        translated = encrypt_message(message, key)
    elif mode == 'decrypt':
        translated = decrypt_message(message, key)
    else:
        raise

    print()
    print(f'{mode.title()}ed message:')
    print(translated)
    print()

    try:
        pyperclip.copy(translated)
    except Exception as e:
        print(e)
        pass
    else:
        print(f'Full {mode}ed message was copied to clipboard!')


def encrypt_message(message, key):
    return translate_message(message, key, mode='encrypt')


def decrypt_message(message, key):
    return translate_message(message, key, mode='decrypt')


def translate_message(message, key, mode):
    translated = []

    key_index = 0
    key = key.upper()

    for char in message:
        num = LETTERS.find(char.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[key_index])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[key_index])

            num %= len(LETTERS)

            if char.isupper():
                translated.append(LETTERS[num])
            elif char.islower():
                translated.append(LETTERS[num].lower())

            key_index += 1
            if key_index == len(key):
                key_index = 0

        else:
            translated.append(char)

    return ''.join(translated)


if __name__ == '__main__':
    main()

import pyperclip


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('Caesar Cipher!')
    print('The Caesar Cipher encrypts letters by shifting them over by a key number.')
    print()

    key = 0

    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt message?')
        response = input('> ').lower()
        if response in ('e', 'encrypt'):
            mode = 'encrypt'
            break
        elif response in ('d', 'decrypt'):
            mode = 'decrypt'
            break
        print('Please, enter e or d letter!')

    while True:
        max_key = len(SYMBOLS) - 1
        print(f'Please, enter the key number from 0 to {max_key}')
        response = input('> ')
        if not response.isdecimal():
            continue
        if 0 <= int(response) < len(SYMBOLS):
            key = int(response)
            break

    print(f'Enter the message to {mode}: ')
    message = input('> ').upper().rstrip()

    translated_message = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)

            if mode == 'encrypt':
                num += key
            elif mode == 'decrypt':
                num -= key

            if num >= len(SYMBOLS):
                num -= len(SYMBOLS)
            elif num < 0:
                num += len(SYMBOLS)

            translated_message += SYMBOLS[num]
        else:
            translated_message += symbol

    print(translated_message)

    try:
        pyperclip.copy(translated_message)
        print(f'Full {mode}ed text copied to clipboard!')
    except:
        pass


if __name__ == '__main__':
    main()

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('Caesar Cipher Hacker!')
    print('Enter encrypted Caesar Cipher message to hack: ')
    message = input('> ')

    for key in range(len(SYMBOLS)):
        translated_message = ''

        for symbol in message:
            if symbol in SYMBOLS:
                num = SYMBOLS.find(symbol)
                num -= key

                if num < 0:
                    num += len(SYMBOLS)

                translated_message += SYMBOLS[num]
            else:
                translated_message += symbol

        print(f'Key #{key}: {translated_message}')


if __name__ == '__main__':
    main()

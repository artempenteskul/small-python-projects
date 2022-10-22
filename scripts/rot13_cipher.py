import sys
import pyperclip


UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def main():
    print('The Rot13 Cipher Script.')
    print()

    while True:
        print('Enter the message to encrypt/decrypt using Rot13 Cipher (or QUIT): ')
        message = input('> ')

        if message.upper() == 'QUIT':
            print()
            print('Job is done. Bye!')
            sys.exit()

        translated = ''
        for char in message:
            if char.isupper():
                translated_char_index = (UPPER_LETTERS.find(char) + 13) % 26
                translated += UPPER_LETTERS[translated_char_index]
            elif char.islower():
                translated_char_index = (LOWER_LETTERS.find(char) + 13) % 26
                translated += LOWER_LETTERS[translated_char_index]
            else:
                translated += char

        print()
        print('Translated message is: ')
        print(translated)

        try:
            pyperclip.copy(translated)
            print()
            print('Copied to clipboard!')
        except Exception as e:
            print(f'The exception while copying to clipboard: {e}')
            pass


if __name__ == '__main__':
    main()

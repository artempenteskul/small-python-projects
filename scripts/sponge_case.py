import random
import pyperclip


def main():
    print('Sponge Case Script.')
    print('This program allows you to translate your message to sPoNgEcAsE')
    print()

    print('Enter message to convert: ')
    response = input('> ')

    converted = convert_to_sponge_case(response)
    print()
    print(converted)
    print()

    try:
        pyperclip.copy(converted)
    except:
        pass
    else:
        print('Copied to clipboard!')


def convert_to_sponge_case(text):
    sponge_text = ''
    is_upper = False
    for char in text:
        if not char.isalpha():
            sponge_text += char
        elif is_upper:
            sponge_text += char.upper()
        elif not is_upper:
            sponge_text += char.lower()

        is_upper = not is_upper

    return sponge_text


if __name__ == '__main__':
    main()

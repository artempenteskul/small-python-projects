import random
import pyperclip


def main():
    print('The Leetspeak converter script!')
    print()
    print('Enter your message: ')
    message = input('> ')
    leetspeak_message = message_to_leetspeak(message)
    print()
    print(leetspeak_message)

    try:
        pyperclip.copy(leetspeak_message)
    except NameError:
        pass
    else:
        print()
        print('Copied to clipboard!')


def message_to_leetspeak(message):
    CHAR_TO_LEETSPEAK = {
        'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
        'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'],
        'k': [']<'], 'o': ['0'], 's': ['$', '5'],
        't': ['7', '+'], 'u': ['|_|'], 'v': ['\\/']
    }

    leetspeak_message = ''

    for char in message:
        if char.lower() in CHAR_TO_LEETSPEAK and random.random() <= 0.7:
            possible_replacements = CHAR_TO_LEETSPEAK[char.lower()]
            leetspeak_message += random.choice(possible_replacements)
        else:
            leetspeak_message += char

    return leetspeak_message


if __name__ == '__main__':
    main()

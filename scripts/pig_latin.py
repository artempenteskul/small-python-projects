import pyperclip


VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')


def main():
    print('The Pig Latin Script!')
    print('This program translates messages from English to Pig Latin language.')
    print()

    print('Enter your message: ')
    message = input('> ')
    pig_latin_message = to_pig_latin(message)
    print(pig_latin_message)

    try:
        pyperclip.copy(pig_latin_message)
        print('Copied Pig Latin message to clipboard!')
    except Exception as e:
        print(e)
        pass


def to_pig_latin(message):
    pig_latin_message = ''
    for word in message.split():
        prefix_non_letters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]
        if len(word) == 0:
            pig_latin_message = f'{pig_latin_message}{prefix_non_letters} '
            continue

        suffix_non_letters = ''
        while not word[-1].isalpha():
            suffix_non_letters = word[-1] + suffix_non_letters
            word = word[:-1]

        was_upper = word.isupper()
        was_title = word.istitle()

        word = word.lower()

        prefix_consonants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefix_consonants += word[0]
            word = word[1:]

        if prefix_consonants != '':
            word += prefix_consonants + 'ay'
        else:
            word += 'yay'

        if was_upper:
            word = word.upper()
        elif was_title:
            word = word.title()

        pig_latin_message += prefix_non_letters + word + suffix_non_letters + ' '

    return pig_latin_message


if __name__ == '__main__':
    main()

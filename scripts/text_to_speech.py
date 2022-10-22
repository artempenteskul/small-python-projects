import sys
import pyttsx3


def main():
    try:
        tts = pyttsx3.init()

        print('The text to speech program!')
        print('Convert your text to speech!')
        print()

        print('Enter your message: ')
        text = input('> ')

        tts.say(text)
        tts.runAndWait()

    except Exception as e:
        print(f'An error occurred: {e}')
        print('Try again later.')
        sys.exit()


if __name__ == '__main__':
    main()

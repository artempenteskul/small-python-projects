import time
import random


REPLIES = [
    'LET ME THINK ON THIS...',
    'AN INTERESTING QUESTION...',
    'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
    'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
    'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
    'YES... NO... MAYBE... I WILL THINK ON IT...',
    'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...',
    'I SHALL CONSULT MY VISIONS...',
    'YOU MAY WANT TO SIT DOWN FOR THIS...',
]

ANSWERS = [
    'YES, FOR SURE',
    'MY ANSWER IS NO',
    'ASK ME LATER',
    'I AM PROGRAMMED TO SAY YES',
    'THE STARS SAY YES, BUT I SAY NO',
    'I DUNNO MAYBE',
    'FOCUS AND ASK ONCE MORE',
    'DOUBTFUL, VERY DOUBTFUL',
    'AFFIRMATIVE',
    'YES, THOUGH YOU MAY NOT LIKE IT',
    'NO, BUT YOU MAY WISH IT WAS SO',
]


def main():
    slow_space_print('The Magic Fortune Ball Program!')
    time.sleep(1)
    slow_space_print('Ask me your YES/NO question ...')
    input('> ')
    print()
    slow_space_print(random.choice(REPLIES))
    slow_space_print('.' * random.randint(5, 12), interval=0.7)
    slow_space_print('I have an answer ...', interval=0.2)
    time.sleep(1)
    slow_space_print(random.choice(ANSWERS), interval=0.05)


def slow_space_print(text, interval=0.1):
    for char in text:
        print(f'{char.upper()} ', end='', flush=True)

        time.sleep(interval)

    print()
    print()


if __name__ == '__main__':
    main()

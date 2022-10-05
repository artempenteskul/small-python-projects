import time
import random


QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6

REWARD = 4
PENALTY = 1

MIN_DICE_VALUE = 1
MAX_DICE_VALUE = 6


def main():
    print('The Dice Math Game!')
    print('Add up all the numbers displayed on the screen.')
    print(f'You have {QUIZ_DURATION} seconds to answer as many as possible.')
    print(f'You get {REWARD} points for right answer and lose {PENALTY} point for each incorrect answer!')

    input('Press Enter to begin ...')

    correct_answers = 0
    incorrect_answers = 0
    counter = 1
    start_time = time.time()

    while time.time() < start_time + time.time():
        dices = []
        for i in range(random.randint(MIN_DICE, MAX_DICE)):
            dice = random.randint(MIN_DICE_VALUE, MAX_DICE_VALUE)
            dices.append(dice)

        sum_answer = sum(dices)

        exercise = ''
        for dice_n, dice_value in enumerate(dices):
            if dice_n == len(dices) - 1:
                exercise += str(dice_value) + '= '
            else:
                exercise += str(dice_value) + '+'

        answer = input(f'EXERCISE #{counter}: {exercise}')

        if answer == sum_answer:
            correct_answers += 1
        else:
            incorrect_answers += 1

        counter += 1

    score = (correct_answers * REWARD) + (incorrect_answers * PENALTY)
    print(f'Your overall score: {score}')
    print(f'Quiz duration: {QUIZ_DURATION} seconds.')
    print(f'Exercises quantity: {counter}.')
    print(f'Correct answers: {correct_answers}.')
    print(f'Incorrect answers: {incorrect_answers}.')
    print('Thanks for playing, bye!')


if __name__ == '__main__':
    main()

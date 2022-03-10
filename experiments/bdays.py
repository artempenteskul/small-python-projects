import datetime
import random


def getBirthdays(numberOfBirthdays: int):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2022, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatchBirthdays(birthdays: list):
    if len(birthdays) == len(set(birthdays)):
        return None

    for birthdayIndex, birthdayValue in enumerate(birthdays):
        if birthdayValue in birthdays[birthdayIndex + 1:]:
            return birthdayValue


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


def main():
    print(
        '''
            Birthday Paradox by Monte-Carlo method.
            
            The Birthday Paradox shows us that in a group of N people, the odds
            that two of them have matching birthdays is surprisingly large.
            This program does a Monte Carlo simulation (that is, repeated random simulations) to explore this concept.
            
            (It's not actually a paradox, it's just a surprising result.) 
        '''
    )

    while True:
        print('How many birthdays should I generate for each attempt: ')
        response = input('> ')
        if response.isdecimal() and 0 < int(response) <= 100:
            numberOfDays = int(response)
            break

    print(f'\nHere are {numberOfDays} birthdays: ')
    birthdays = getBirthdays(numberOfBirthdays=numberOfDays)

    for birthdayIndex, birthdayValue in enumerate(birthdays):
        if birthdayIndex != 0:
            print(', ', end='')
        monthName = MONTHS[birthdayValue.month - 1]
        dateText = f'{monthName} {birthdayValue.day}'
        print(dateText, end='')

    match = getMatchBirthdays(birthdays)

    print('\nIn this simulation: ')

    if match is not None:
        monthName = MONTHS[match.month - 1]
        dateText = f'{monthName} {match.day}'
        print(f'Multiple people have birthday on this day: {dateText}')
    else:
        print('There are no matching birthdays')

    print(f'Generating {numberOfDays} random birthdays 100.000 times...')
    input('Press any key to begin...')
    print('Let\'s run another 100.000 simulations')

    matchQuantity = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(f'{i} simulations ...')
        birthdays = getBirthdays(numberOfBirthdays=numberOfDays)
        if getMatchBirthdays(birthdays) is not None:
            matchQuantity += 1
    print('100 000 simulations are run.')

    probability = round(matchQuantity / 100_000 * 100, 2)
    print(f'Probability that 2 people in group of {numberOfDays} people have birthday on the same day: {probability}%')
    print('There\'s probably more than you would think!')


if __name__ == '__main__':
    main()

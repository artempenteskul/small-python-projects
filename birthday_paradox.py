import datetime
import random


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


def get_birthdays(birthdays_quantity):
    birthdays = []
    for i in range(birthdays_quantity):
        start_date = datetime.date(2000, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthdays.append(start_date + random_number_of_days)
    return birthdays


def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for birthday in birthdays:
        if birthdays.count(birthday) > 1:
            return birthday


def main():
    print('Birthday paradox examination using Monte Carlo simulation')

    while True:
        print('How many b-days should I generate? (max 100)')
        response = input('> ')
        if response.isdecimal() and (0 < int(response) <= 100):
            num_of_birthdays = int(response)
            break

    print()

    print(f'Here are {num_of_birthdays} birthdays: ')
    birthdays = get_birthdays(num_of_birthdays)
    for birthday_n, birthday in enumerate(birthdays):
        if birthday_n != 0:
            print(', ', end='')
        month_name = MONTHS[birthday.month - 1]
        birthday_date_str = f'{month_name} {birthday.day}'
        print(birthday_date_str, end='')

    print()

    match = get_match(birthdays)
    print('Result of simulation:')
    if match is not None:
        month_name = MONTHS[match.month - 1]
        match_date_str = f'{month_name} {match.day}'
        print(f'Multiple people have birthday on {match_date_str}!')
    else:
        print('There are no matching birthdays!')

    print()

    print(f'Generating {num_of_birthdays} birthdays 100_000 times')
    input('> Press Enter to begin ...')

    print('Let\'s run another 100_000 simulations.')
    match_counter = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(f'{i} simulations run ...')
        birthdays = get_birthdays(num_of_birthdays)
        if get_match(birthdays) is not None:
            match_counter += 1

    print('100_000 simulations run !')

    probability = round(match_counter / 100_000 * 100, 2)
    print(f'Number of birthdays: {num_of_birthdays}')
    print(f'Probability of match: {probability}%')


if __name__ == '__main__':
    main()

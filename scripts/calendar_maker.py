import datetime


DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December')


def main():
    print('This is Calendar Maker!')
    user_year = get_year_from_user()
    user_month = get_month_from_user()
    user_calendar = get_calendar(user_year, user_month)

    print(user_calendar)

    user_calendar_filename = f'calendar_{MONTHS[user_month - 1]}_{user_year}.txt'
    with open(user_calendar_filename, 'w') as calendar_obj:
        calendar_obj.write(user_calendar)

    print(f'Your calendar was saved to {user_calendar_filename}!')


def get_year_from_user():
    year = None
    while True:
        print('Enter the year for the calendar: ')
        response = input('> ')

        if response.isdecimal() and int(response) > 0:
            year = int(response)
            break

        print('Please, enter a numeric year, like 2002.')
        continue

    return year


def get_month_from_user():
    month = None
    while True:
        print('Enter the month for the calendar: ')
        response = input('> ')

        if response.isdecimal() and (1 <= int(response) <= 12):
            month = int(response)
            break

        print('Please, enter a numeric month, like 3 for March.')
        continue

    return month


def get_calendar(year, month):
    calendar_text = ''
    calendar_text += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    calendar_text += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    week_separator = ('+----------' * 7) + '+\n'
    blank_row = ('|          ' * 7) + '|\n'

    current_date = datetime.date(year, month, 1)

    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:
        calendar_text += week_separator

        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1)

        day_number_row += '|\n'
        calendar_text += day_number_row
        for i in range(3):
            calendar_text += blank_row

        if current_date.month != month:
            break

    calendar_text += week_separator
    return calendar_text


if __name__ == '__main__':
    main()

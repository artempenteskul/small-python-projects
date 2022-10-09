import sys


def main():
    print('The Fibonacci Sequence Program!')
    print('The Fibonacci Sequence begins with 0 and 1, and the next number is the sum of the previous two numbers.')
    print('The sequence continues forever ...')

    while True:
        print('Enter the n-th Fibonacci number (or QUIT): ')
        response = input('> ')

        if response.lower().startswith('q'):
            print('Bye!')
            sys.exit()

        if not (response.isdecimal() and int(response) >= 0):
            print('Your input was incorrect. Try again!')
            continue

        nth = int(response)

        if nth == 1:
            print('0')
            print()
            print('The Fibonacci Number is: 0')
        elif nth == 2:
            print('1')
            print()
            print('The Fibonacci Number is: 1')

        if nth >= 10_000:
            print('WARNING! This will take a while to display on the screen.')
            input('Press Enter to begin ...')

        second_last_number = 0
        last_number = 1
        fib_numbers_count = 2
        print('0, 1, ', end='')

        while True:
            next_num = second_last_number + last_number
            fib_numbers_count += 1

            print(next_num, end='')

            if fib_numbers_count == nth:
                print()
                print()
                print(f'The {nth} Fibonacci Number is {next_num}! You can check it manually if you want!')
                break

            print(', ', end='')

            second_last_number = last_number
            last_number = next_num


if __name__ == '__main__':
    main()

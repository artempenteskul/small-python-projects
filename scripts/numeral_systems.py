def main():
    print('The Numeral System Counters!')
    print('This program shows you equivalent numbers in decimal (base 10), hexadecimal (base 16), and binary (base 2) numeral systems.')
    print()
    print('Press Ctrl-C to quit ...')
    print()

    while True:
        print('Enter the starting number (e.g. 0): ')
        response = input('> ')
        if response == '':
            response = '0'
            break
        if response.isdecimal():
            break
        print('Please enter a number greater than or equal to 0.')

    start = int(response)

    while True:
        print('Enter how many numbers to display (e.g. 1000): ')
        response = input('> ')
        if response == '':
            response = '0'
            break
        if response.isdecimal():
            break
        print('Please enter a number.')

    amount = int(response)

    for number in range(start, start + amount):
        hex_num = hex(number)[2:].upper()
        bin_num = bin(number)[2:]
        oct_num = oct(number)[2:].upper()

        print(f'BIN: {bin_num} -- OCT: {oct_num} -- DEC: {number} -- HEX: {hex_num}')


if __name__ == '__main__':
    main()

def main():
    print('The Gullible Experiment!')

    while True:
        print('Do you want to know how to keep a gullible person busy for hours? Y/N')
        response = input('> ').lower()

        if response == 'no' or response == 'n':
            break

        if response == 'y' or response == 'yes':
            continue

        print(f'{response} is not a valid y/n response! Try again.')

    print('Thanks for the experiment!')


if __name__ == '__main__':
    main()

X_REPEAT = 30
Y_REPEAT = 20


def main():
    for y in range(Y_REPEAT):
        for x in range(X_REPEAT):
            print(r'/ \_', end='')

        print()

        for x in range(X_REPEAT):
            print(r'\_/ ', end='')

        print()


if __name__ == '__main__':
    main()

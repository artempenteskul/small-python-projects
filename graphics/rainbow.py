import sys
import time
import bext


def main():
    print('The Rainbow Graphics Program!')
    print()
    print('Press Ctrl-C to stop ...')
    time.sleep(2)

    indent = 0
    indent_increasing = True

    try:
        while True:
            print(' ' * indent, end='')
            bext.fg('red')
            print('##', end='')
            bext.fg('yellow')
            print('##', end='')
            bext.fg('green')
            print('##', end='')
            bext.fg('blue')
            print('##', end='')
            bext.fg('cyan')
            print('##', end='')
            bext.fg('purple')
            print('##')

            if indent_increasing:
                indent += 1
                if indent >= 60:
                    indent_increasing = False

            else:
                indent -= 1
                if indent == 0:
                    indent_increasing = True

            time.sleep(0.2)

    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()

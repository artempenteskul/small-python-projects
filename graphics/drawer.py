import sys
import shutil


UP_DOWN_CHAR = chr(9474)
LEFT_RIGHT_CHAR = chr(9472)
DOWN_RIGHT_CHAR = chr(9484)
DOWN_LEFT_CHAR = chr(9488)
UP_RIGHT_CHAR = chr(9492)
UP_LEFT_CHAR = chr(9496)
UP_DOWN_RIGHT_CHAR = chr(9500)
UP_DOWN_LEFT_CHAR = chr(9508)
DOWN_LEFT_RIGHT_CHAR = chr(9516)
UP_LEFT_RIGHT_CHAR = chr(9524)
CROSS_CHAR = chr(9532)

CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -= 1
CANVAS_HEIGHT -= 5


def main():
    canvas = {}
    cursor_x = 0
    cursor_y = 0

    moves = []
    while True:
        print(get_canvas_string(canvas, cursor_x, cursor_y))
        print('WASD keys to move, H for help, C to clear, F to save, Q to quit.')
        response = input('> ').upper()

        if response == 'Q':
            print('Thanks for playing!')
            sys.exit()
        elif response == 'H':
            print('Enter WASD characters to move and draw the line. Try it yourself!')
            print('You can save the picture entering the F.')
            input('Press Enter to continue ...')
            continue
        elif response == 'C':
            canvas = {}
            moves.append('C')
        elif response == 'F':
            try:
                print('Enter the filename to save the picture: ')
                filename = input('> ')

                if not filename.endswith('.txt'):
                    filename += '.txt'
                with open(filename, 'w') as file:
                    file.write(''.join(moves) + '\n')
                    file.write(get_canvas_string(canvas, None, None))
            except Exception as e:
                print(f'ERROR: Could not save the file due to: {str(e)}')

        for command in response:
            if command not in ('W', 'A', 'S', 'D'):
                continue

            moves.append(command)

            if canvas == {}:
                if command in ('W', 'S'):
                    canvas[(cursor_x, cursor_y)] = {'W', 'S'}
                elif command in ('A', 'D'):
                    canvas[(cursor_x, cursor_y)] = {'A', 'D'}

            if command == 'W' and cursor_y > 0:
                canvas[(cursor_x, cursor_y)].add(command)
                cursor_y -= 1
            elif command == 'S' and cursor_y < CANVAS_HEIGHT - 1:
                canvas[(cursor_x, cursor_y)].add(command)
                cursor_y += 1
            elif command == 'A' and cursor_x > 0:
                canvas[(cursor_x, cursor_y)].add(command)
                cursor_x -= 1
            elif command == 'D' and cursor_x < CANVAS_WIDTH - 1:
                canvas[(cursor_x, cursor_y)].add(command)
                cursor_x += 1
            else:
                continue

            if (cursor_x, cursor_y) not in canvas:
                canvas[(cursor_x, cursor_y)] = {}

            if command == 'W':
                canvas[(cursor_x, cursor_y)].add('S')
            elif command == 'S':
                canvas[(cursor_x, cursor_y)].add('W')
            elif command == 'A':
                canvas[(cursor_x, cursor_y)].add('D')
            elif command == 'D':
                canvas[(cursor_x, cursor_y)].add('A')


def get_canvas_string(canvas_data, x, y):
    canvas_str = ''
    for row_num in range(CANVAS_HEIGHT):
        for column_num in range(CANVAS_WIDTH):
            if column_num == x and row_num == y:
                canvas_str += '#'
                continue

            cell = canvas_data.get((column_num, row_num))
            if cell in ({'W', 'S'}, {'W'}, {'S'}):
                canvas_str += UP_DOWN_CHAR
            elif cell in ({'A', 'D'}, {'A'}, {'D'}):
                canvas_str += LEFT_RIGHT_CHAR
            elif cell == {'S', 'D'}:
                canvas_str += DOWN_RIGHT_CHAR
            elif cell == {'A', 'S'}:
                canvas_str += DOWN_LEFT_CHAR
            elif cell == {'W', 'D'}:
                canvas_str += UP_RIGHT_CHAR
            elif cell == {'W', 'A'}:
                canvas_str += UP_LEFT_CHAR
            elif cell == {'W', 'S', 'D'}:
                canvas_str += UP_DOWN_RIGHT_CHAR
            elif cell == {'A', 'S', 'D'}:
                canvas_str += DOWN_LEFT_RIGHT_CHAR
            elif cell == {'W', 'A', 'D'}:
                canvas_str += UP_LEFT_RIGHT_CHAR
            elif cell == {'W', 'A', 'S', 'D'}:
                canvas_str += CROSS_CHAR
            elif cell is None:
                canvas_str += ' '

        canvas_str += '\n'

    return canvas_str


if __name__ == '__main__':
    main()

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

canvas = {}
cursor_x = 0
cursor_y = 0


def main():
    moves = []
    while True:
        print(get_canvas_string(canvas, cursor_x, cursor_y))
        print('WASD keys to move, H for help, C to clear, F to save, Q to quit.')
        response = input('> ').upper()

        if response == 'Q':
            print('Thanks for playing!')
            sys.exit()


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

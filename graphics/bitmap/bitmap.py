import sys


print('This is bitmap program')
print('Enter the message to display with the bitmap')
message = input('> ')

if message == '':
    print('You haven\'t entered the message. Start program again')
    sys.exit()

try:
    file = open('bitmapworld.txt', 'r')
except IOError:
    print('Error while file opening')
    sys.exit()

for line in file:
    for elementIndex, elementValue in enumerate(line):
        if elementValue == ' ':
            print(' ', end='')
        else:
            print(message[elementIndex % len(message)], end='')
    print()
file.close()

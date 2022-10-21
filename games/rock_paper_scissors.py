import sys
import time
import random


RPS = {
    'R': 'ROCK',
    'P': 'PAPER',
    'S': 'SCISSORS'
}


def main():
    print('Rock, Paper, Scissors!')
    print('Rock beats Scissors')
    print('Paper beats Rock')
    print('Scissors beats Paper')
    print()

    wins = 0
    losses = 0
    ties = 0

    while True:
        while True:
            print('Enter your move (R)ock, P(aper), S(cissors) or Q(uit): ')
            player_move = input('> ').upper()

            if player_move == 'Q':
                print('Thanks for playing!')
                sys.exit()

            if player_move in ('R', 'P', 'S'):
                break
            else:
                print('Type one of R, P, S or Q to quit.')

        player_move = RPS.get(player_move)
        print(f'{player_move} versus ...')

        time.sleep(0.25)
        print('1...')
        time.sleep(0.25)
        print('2...')
        time.sleep(0.25)
        print('3...')
        time.sleep(0.25)

        computer_move = random.choice(list(RPS.values()))
        print(computer_move)
        print()
        time.sleep(0.5)

        if player_move == computer_move:
            print('It\'s a tie!')
            ties += 1
        elif (player_move == 'ROCK' and computer_move == 'SCISSORS'
              or player_move == 'SCISSORS' and computer_move == 'PAPER'
              or player_move == 'PAPER' and computer_move == 'ROCK'):
            print()
            print('You win!')
            wins += 1
        elif (player_move == 'SCISSORS' and computer_move == 'ROCK'
              or player_move == 'PARER' and computer_move == 'SCISSORS'
              or player_move == 'ROCK' and computer_move == 'PAPER'):
            print()
            print('You lose!')
            losses += 1

        print()

        print(f'{wins} Wins - {losses} Losses - {ties} Ties')
        print()


if __name__ == '__main__':
    main()

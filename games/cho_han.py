import sys
import random


JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}


def main():
    print('The Cho-Han game!')
    print('In this traditional Japanese dice game, two dice are rolled in a bamboo cup by dealer.')
    print('The player must guess if the dice total to an even (cho) or odd (han) number.')
    print()

    money = 5000
    while True:
        print(f'You have {money} mon!')
        print('How much do you wanna bet? (or QUIT): ')
        while True:
            response = input('> ')
            if response.lower().startswith('q'):
                print('Thanks for game! Good luck!')
                sys.exit()
            elif not response.isdecimal() or int(response) < 0:
                print('Please, enter positive number!')
            elif int(response) > money:
                print('You do not have enough to make that bet.')
            else:
                bet = int(response)
                break

        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        print('The dealer swirls the cup and you hear the rattle of dice.')
        print('YOUR BET: CHO (even) or HAN (odd)? ')

        while True:
            answer = input('> ').upper().rstrip()
            if answer != 'CHO' and answer != 'HAN':
                print('Please, enter "CHO" (even) or "HAN" (odd)!')
                continue
            break

        print()
        print('The dealer lifts the cup to reveal: ')
        print(f'{JAPANESE_NUMBERS[dice_1]} - {JAPANESE_NUMBERS[dice_2]}')
        print(f'{dice_1} - {dice_2}')

        is_roll_even = (dice_1 + dice_2) % 2 == 0

        if is_roll_even:
            correct_answer = 'CHO'
        else:
            correct_answer = 'HAN'

        is_player_won = answer == correct_answer

        if is_player_won:
            print(f'You won! You take {bet} mon!')
            money += bet
            print(f'The playing house collects a {bet // 10} mon fee.')
            money -= bet // 10
            print()
        else:
            money -= bet
            print(f'You lost!')
            print()

        if money == 0:
            print('You have run out of money!')
            print('Thanks for playing!')
            sys.exit()


if __name__ == '__main__':
    main()

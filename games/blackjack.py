import sys
import random


HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

MONEY_AMOUNT = 5000


def main():
    print('Blackjack game!')
    print('--- Rules ---')
    print('Try to get as close to 21 without going over!')
    print('Kings, Queens and Jacks are worth 10 points')
    print('Aces are worth 1 or 11 points')
    print('Cards 2 through 10 worth their face value')
    print()
    print('(H)it to take another card.')
    print('(S)tand to stop taking cards.')
    print('On your first play, you can (D)ouble down to increase your bet')
    print()
    print('In case of a tie, the bet is returned to the player.')

    money = MONEY_AMOUNT
    while True:
        if money <= 0:
            print('You\'re broke!')
            print('Good thing you weren\'t playing with real money.')
            print('Good luck, loser!')
            sys.exit()

        print(f'Money: {money}')
        bet = get_bet(money, money)

        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        print(f'Bet: {bet}')
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()

            if get_hand_value(player_hand) > 21:
                break

            move = get_move(player_hand, money - bet)

            print(move)
            print()

            if move.upper() == 'D':
                additional_bet = get_bet(min(bet, (money - bet)), money)
                bet += additional_bet
                print(f'Bet increased to ${bet}')
                print(f'Bet: {bet}')

            if move.upper() in ('H', 'D'):
                new_card = deck.pop()
                rank, suit = new_card
                print(f'You drew a {rank} of {suit}')
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    continue

            if move.upper() in ('S', 'D'):
                break

        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break

                input('Press Enter to continue ...')
                print()

        display_hands(player_hand, dealer_hand, True)
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        if dealer_value > 21:
            print(f'Dealer busts! You win ${bet}!')
            money += bet
        elif (player_value > 21) or (dealer_value > player_value):
            print('You lost!')
            money -= bet
        elif player_value > dealer_value:
            print(f'You won ${bet}!')
            money += bet
        elif player_value == dealer_value:
            print('It\'s tie! The bet is returned to you!')

        input('Press Enter to continue ...')
        print()


def get_bet(max_bet, money):
    while True:
        print(f'How much do you bet? (1-{max_bet} or QUIT)')
        bet = input('> ').upper().strip()

        if bet in ('Q', 'QUIT'):
            result_of_game = abs(money - MONEY_AMOUNT)
            print(f'--- Result of your game ---')
            print(f'You\'ve lost ${result_of_game}!') if result_of_game < 0 else print(f'You\'ve earned ${result_of_game}')
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet


def get_deck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'K', 'Q', 'A'):
            deck.append((str(rank), suit))

    random.shuffle(deck)
    return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    print()

    if show_dealer_hand:
        print(f'DEALER: {get_hand_value(dealer_hand)}')
        display_cards(dealer_hand)
    else:
        print(f'DEALER: ???')
        display_cards(dealer_hand, True)

    print(f'PLAYER: {get_hand_value(player_hand)}')
    display_cards(player_hand)


def get_hand_value(hand):
    value = 0
    number_of_aces = 0

    for card in hand:
        rank = card[0]
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10

    return value


def display_cards(hand, show_backside=False):
    for card in hand:
        card_str = '??' if show_backside else f'{card[0]}{card[1]}'
        if card == hand[-1]:
            print(card_str)
        else:
            print(card_str, end=' ')


def get_move(hand, money):
    while True:
        possible_moves = ['(H)it', '(S)tand']
        if len(hand) == 2 and money > 0:
            possible_moves.append('(D)ouble down')

        move_prompt = ','.join(possible_moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in possible_moves:
            return move


if __name__ == '__main__':
    main()

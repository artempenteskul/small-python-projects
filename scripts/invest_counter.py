ANNUAL_PERCENT = 0.08
ANNUAL_DIVIDEND_PERCENT = 0.025


def main():
    print('The Invest Counter Script!')
    print('This is simple (silly) invest counter script which counts your minimal invest earnings.')
    print()

    invest_duration = get_invest_duration()
    annual_replenishment = get_annual_replenishment()

    print()
    print(f'Your start capital for first year: ${annual_replenishment}.')
    input('Press Enter to start simulation ...')
    print()

    dividends = 0
    earnings = 0
    capital = annual_replenishment

    for i in range(invest_duration):
        start_year_capital = capital
        annual_earnings = count_annual_earnings(capital)
        annual_dividends = count_annual_dividends(capital)

        dividends += annual_dividends
        earnings += annual_earnings
        capital += (annual_earnings + annual_dividends)

        print(f'--- YEAR #{i+1} ---')
        print(f'Start year capital: ${start_year_capital:.2f}')
        print(f'Annual earnings: ${annual_earnings:.2f}')
        print(f'Annual dividends: ${annual_dividends:.2f}')
        print(f'End year capital: ${capital:.2f}')

        capital += annual_replenishment

        input('Press Enter to continue ...')
        print()

    print()

    print(f'--- Overall results ---')
    print(f'Money spent in {invest_duration} years: ${invest_duration * annual_replenishment:.2f}')
    print(f'End capital: ${capital:.2f}')
    print(f'Total earnings sum: ${earnings:.2f}')
    print(f'Dividends sum: ${dividends:.2f}')

    print()

    print(f'Money earned: ${capital - (invest_duration * annual_replenishment):.2f}')


def get_invest_duration():
    response = ''
    while not response.isdecimal():
        response = input('Enter how many years do you wanna invest: ')

    print(f'Program takes your invest duration as {int(response)} years.')

    return int(response)


def get_annual_replenishment():
    response = ''
    while not response.isdecimal():
        response = input('Enter how much money per year can you add in average to your capital in $: ')

    print(f'Program takes your annual replenishment as ${float(response)}')

    return float(response)


def count_annual_earnings(capital):
    annual_earnings = capital * ANNUAL_PERCENT
    return annual_earnings


def count_annual_dividends(capital):
    annual_dividends = capital * ANNUAL_DIVIDEND_PERCENT
    return annual_dividends


if __name__ == '__main__':
    main()

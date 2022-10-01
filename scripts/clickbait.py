import random


OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']

NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent', 'Cat', 'Dog',
         'Chicken', 'Robot', 'Video Game', 'Avocado', 'Plastic Straw','Serial Killer', 'Telephone Psychic']

STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']

PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement', 'Workplace', 'Donut Shop', 'Apocalypse Bunker']

WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

WEBSITES = ['Facebuuk', 'Googles', 'Facesbook', 'Tweedie', 'Pastagram']


class TemplateDoesNotExist(Exception):
    pass


def main():
    print('The Clickbait Headline Generator!')
    print()

    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number clickbait headlines to generate: ')
        response = input('> ')
        if not response.isdecimal() or int(response) < 0:
            print('Please, enter a positive number!')
        else:
            number_of_headlines = int(response)
            break

    for i in range(number_of_headlines):
        clickbait_type = random.randint(1, 8)

        if clickbait_type == 1:
            headline = generate_killing_headline()
        elif clickbait_type == 2:
            headline = generate_you_dont_know_headline()
        elif clickbait_type == 3:
            headline = generate_big_companies_haters_headline()
        elif clickbait_type == 4:
            headline = generate_you_wont_believe_headline()
        elif clickbait_type == 5:
            headline = generate_dont_you_want_to_know_headline()
        elif clickbait_type == 6:
            headline = generate_gift_idea_headline()
        elif clickbait_type == 7:
            headline = generate_reasons_why_headline()
        elif clickbait_type == 8:
            headline = generate_job_automated_headline()
        else:
            raise TemplateDoesNotExist(f'Template with number {clickbait_type} does not exist!')

        print(headline)
    print()

    website = random.choice(WEBSITES)
    when = random.choice(WHEN)
    print(f'Post these headlines to our {website} {when} or you\'re fired!')


def generate_killing_headline():
    noun = random.choice(NOUNS)
    return f'Are Millennials Killing the {noun} Industry?'


def generate_you_dont_know_headline():
    noun = random.choice(NOUNS)
    plural_noun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return f'Without This {noun}, {plural_noun} Could Kill You {when}!'


def generate_big_companies_haters_headline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun_1 = random.choice(NOUNS)
    noun_2 = random.choice(NOUNS)
    return f'Big Companies Hate {pronoun}! See How This {state} {noun_1} Invented a Cheaper {noun_2}'


def generate_you_wont_believe_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f'You Won\'t Believe What This {state} {noun} Found in {pronoun} {place}'


def generate_dont_you_want_to_know_headline():
    plural_noun_1 = random.choice(NOUNS) + 's'
    plural_noun_2 = random.choice(NOUNS) + 's'
    return f'What {plural_noun_1} Don\'t Want You To Know About {plural_noun_2}?'


def generate_gift_idea_headline():
    number = random.randint(7, 22)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return f'{number} Gift Ideas to Give Your {noun} From {state}!'


def generate_reasons_why_headline():
    number_1 = random.randint(3, 21)
    plural_noun = random.choice(NOUNS) + 's'
    number_2 = random.randint(1, number_1)
    return f'{number_1} Reasons Why {plural_noun} Are More Interesting Than You Think (Number {number_2} Will Surprise You!)'


def generate_job_automated_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun_1 = POSSESIVE_PRONOUNS[i]
    pronoun_2 = PERSONAL_PRONOUNS[i]
    if pronoun_1 == 'Their':
        return f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun_1} Job. {pronoun_2} Were Wrong.'
    else:
        return f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun_1} Job. {pronoun_2} Was Wrong.'


if __name__ == '__main__':
    main()

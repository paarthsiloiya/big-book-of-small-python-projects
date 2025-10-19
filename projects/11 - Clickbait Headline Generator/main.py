import random

OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan',
          'Arizona', 'Washington', 'Colorado', 'Oregon', 'Nevada']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw','Serial Killer', 'Telephone Psychic', 'Influencer',
         'Cryptocurrency', 'Pizza', 'Yoga Instructor', 'Politician',
         'Smartphone', 'Coffee', 'Vegetarian', 'Uber Driver', 'Programmer']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker', 'Garage',
          'Bathroom', 'Garden', 'Car', 'Storage Unit', 'Closet']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week',
        'By Tomorrow', 'In Days', 'Before 2026']
ADJECTIVES = ['Shocking', 'Unbelievable', 'Surprising', 'Mind-Blowing',
              'Bizarre', 'Incredible', 'Outrageous', 'Crazy']
VERBS = ['Revolutionize', 'Transform', 'Destroy', 'Save', 'Change',
         'Improve', 'Ruin', 'Enhance']


website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                            'Facesbook', 'Tweedie', 'Pastagram'])
when = random.choice(WHEN).lower()
print('Post these to our', website, when, 'or you\'re fired!')


def generateAreMillenialsKillingHeadline():
    noun = random.choice(NOUNS)
    return 'Are Millenials Killing the {} Industry?'.format(noun)


def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could Kill You {}'.format(noun, pluralNoun, when)


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}'.format(pronoun, state, noun1, noun2)


def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return 'You Won\'t Believe What This {} {} Found in {} {}'.format(state, noun, pronoun, place)


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return 'What {} Don\'t Want You To Know About {}'.format(pluralNoun1, pluralNoun2)


def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1, pluralNoun, number2)


def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(state, noun, pronoun1, pronoun2)


def generateThisOneWeirdTrickHeadline():
    noun = random.choice(NOUNS)
    verb = random.choice(VERBS)
    pluralNoun = random.choice(NOUNS) + 's'
    return 'This One Weird {} Trick Will {} Your {}!'.format(noun, verb, pluralNoun)


def generateScientistsHateHeadline():
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    adjective = random.choice(ADJECTIVES)
    return '{} Scientists Hate This {} Because of Its {} Effect on {}s'.format(state, noun1, adjective, noun2)


def generateCanYouPassHeadline():
    noun = random.choice(NOUNS)
    number = random.randint(5, 12)
    return 'Can You Pass This {} Quiz? Only {}% of People Can!'.format(noun, number * 10)

while True:
    response = input('Enter the number of clickbait headlines to generate: ')
    if not response.isdecimal():
        print('Please enter a number.')
    else:
        numberOfHeadlines = int(response)
        break

for i in range(numberOfHeadlines):
    clickbaitType = random.randint(1, 11)

    if clickbaitType == 1:
        headline = generateAreMillenialsKillingHeadline()
    elif clickbaitType == 2:
        headline = generateWhatYouDontKnowHeadline()
    elif clickbaitType == 3:
        headline = generateBigCompaniesHateHerHeadline()
    elif clickbaitType == 4:
        headline = generateYouWontBelieveHeadline()
    elif clickbaitType == 5:
        headline = generateDontWantYouToKnowHeadline()
    elif clickbaitType == 6:
        headline = generateGiftIdeaHeadline()
    elif clickbaitType == 7:
        headline = generateReasonsWhyHeadline()
    elif clickbaitType == 8:
        headline = generateJobAutomatedHeadline()
    elif clickbaitType == 9:
        headline = generateThisOneWeirdTrickHeadline()
    elif clickbaitType == 10:
        headline = generateScientistsHateHeadline()
    elif clickbaitType == 11:
        headline = generateCanYouPassHeadline()

    print(headline)
print()
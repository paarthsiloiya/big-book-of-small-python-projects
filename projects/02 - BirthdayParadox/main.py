import random, datetime, sys

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def getBirthdays(numberOfBirthdays):
    birthdays = []
    SOY = datetime.date(2006, 1, 1)
    for _ in range(numberOfBirthdays):
        birthdays.append(SOY + datetime.timedelta(random.randint(0, 364)))

    return birthdays
        

def getMatchingBirthdays(birthdays):
    matched_birthdays = []
    for i in range(len(birthdays)):
        for j in range(i + 1, len(birthdays)):
            if birthdays[i] == birthdays[j] and birthdays[i] not in matched_birthdays:
                matched_birthdays.append(birthdays[i])
    return matched_birthdays


def hasMatchingBirthdays(birthdays):
    for i in range(len(birthdays)):
        for j in range(i + 1, len(birthdays)):
            if birthdays[i] == birthdays[j]:
                return True
    return False


def printProgressBar(current, total, bar_length=50):
    progress = current / total
    filled_length = int(bar_length * progress)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    percent = progress * 100
    sys.stdout.write(f'\rProgress: |{bar}| {percent:.1f}% ({current}/{total})')
    sys.stdout.flush()


while True:
    nbday = input("How many birthdays shall I generate? (Max 100): ")
    if nbday.isdigit() and 100 >= int(nbday) > 0:
        nbday = int(nbday)
        break
    
    print("Please enter a valid number between 1 and 100.")

print()
print("Here are", nbday, "birthdays:")
birthdays = getBirthdays(nbday)

for i, birthday in enumerate(birthdays):
    if i != len(birthdays) - 1:
        print(birthday.strftime("%B %d"), end=", ")
    else:
        print(birthday.strftime("%B %d"))

print()

matches = getMatchingBirthdays(birthdays)
print()
if matches:
    print("In this simulation, multiple people have a birthday on:")
    for match in matches:
        print(" ", match.strftime("%B %d"))
else:
    print("In this simulation, there are no matching birthdays.")

print()
NUM_SIMULATIONS = 100000
print(f"Generating {nbday} random birthdays {NUM_SIMULATIONS} times...")
input("Press Enter to begin...")

matches_count = 0

print()
for i in range(NUM_SIMULATIONS):
    sim_birthdays = getBirthdays(nbday)
    if hasMatchingBirthdays(sim_birthdays):
        matches_count += 1
    
    if i % 100 == 0 or i == NUM_SIMULATIONS - 1:
        printProgressBar(i + 1, NUM_SIMULATIONS)

print("\n\n")
print(f"Out of {NUM_SIMULATIONS} simulations of {nbday} people, there was a")
print(f"matching birthday in that group {matches_count} times. This means")
print(f"that {nbday} people have a {round(matches_count / NUM_SIMULATIONS * 100, 2)}% chance of having a matching birthday in their group.")
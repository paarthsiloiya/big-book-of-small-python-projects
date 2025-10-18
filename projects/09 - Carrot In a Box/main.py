import random
import os

p1 = input("Enter player 1 name: ")
p2 = input("Enter player 2 name: ")

playerNames = f"{p1[:11]:^11}    {p2[:11]:^11}\n"

BOX_1, BOX_2 = 'RED', 'GOLD'
n = max(len(BOX_1), len(BOX_2))

print(f'''HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   {BOX_1: <{n}}  | |  |   {BOX_2: <{n}}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/''')

print(playerNames)
print(f"{p1}, you have a {BOX_1} box in front of you.")
print(f"{p2}, you have a {BOX_2} box in front of you.\n")
print(f"{p1}, you will get to look into your box.")
print(f"{p2.upper()}, close your eyes and don't look!!!")

input(f"When {p2} has closed their eyes, press Enter...")

print(f"\n{p1}, here is the inside of your box:")

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print(fr'''
   _________
  |  *  *   |
  | __\/__  |
  |_\    /__|    __________
 /   \  /  /|   /         /|
+---------+ |  +---------+ |
|   {BOX_1: <{n}}  | |  |   {BOX_2: <{n}}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
 ''')
    print(playerNames)
    print(" (carrot!)")

else:
    print(fr'''
   _________
  |         |
  |         |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   {BOX_1: <{n}}  | |  |   {BOX_2: <{n}}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/''')
    print(playerNames)
    print(" (no carrot!)")

input('Press Enter to continue...')
os.system('cls' if os.name == 'nt' else 'clear')
print(f"\nNow, {p2}, you can open your eyes!")

print(f"{p1} say what do you see in your box?")
input(f"{p1}, press Enter to continue...")

while True:
    swapOrNot = input(f"\n{p2}, do you want to swap boxes with {p1}? (yes or no): ").lower()
    if swapOrNot in ('yes', 'y', 'no', 'n'):
        break
    print("Invalid input. Please enter 'yes' or 'no'.")

if swapOrNot in ('yes', 'y'):
    carrotInFirstBox = not carrotInFirstBox
    BOX_1, BOX_2 = BOX_2, BOX_1

print(f"Here are the boxes:")

if carrotInFirstBox:
    print(fr'''
   _________      __________
  |  *  *   |    |         |
  | __\/__  |    |         |
  |_\    /__|    |_________|
 /   \  /  /|   /         /|
+---------+ |  +---------+ |
|   {BOX_1: <{n}}  | |  |   {BOX_2: <{n}}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
 ''')
    print(playerNames)
    print(f"{p1} is the winner! They found the carrot!")

else:
    print(fr'''
   _________      _________  
  |         |    |  *  *   | 
  |         |    | __\/__  | 
  |_________|    |_\    /__|  
 /         /|   /   \  /  /|  
+---------+ |  +---------+ |  
|   {BOX_1: <{n}}  | |  |   {BOX_2: <{n}}  | |
|   BOX   | /  |   BOX   | /  
+---------+/   +---------+/   ''')
    print(playerNames)
    print(f"{p2} is the winner! They found the carrot!")
import random, sys

while True:
    try:
        dice_prompt = input("> ").lower().replace(" ", "")
        if dice_prompt in ('q'):
            print("Exiting Dice Roller. Goodbye!")
            sys.exit()

        dIndex = dice_prompt.index('d')
        if dIndex == -1:
            raise Exception("Missing 'd' in input")

        num_dice = dice_prompt[:dIndex]
        if not num_dice:
            raise Exception("Number of dice is missing")
        elif not num_dice.isdecimal():
            raise Exception("Number of dice must be a number")
        num_dice = int(num_dice)

        modifierIndex = dice_prompt.find('+')
        if modifierIndex == -1:
            modifierIndex = dice_prompt.find('-')
        
        if modifierIndex == -1:
            num_sides = dice_prompt[dIndex + 1:]
            modifier = 0
        else:
            num_sides = dice_prompt[dIndex + 1:modifierIndex]

        if not num_sides:
            raise Exception("Number of sides is missing")
        elif not num_sides.isdecimal():
            raise Exception("Number of sides must be a number")
        num_sides = int(num_sides)

        if modifierIndex != -1:
            modifier_str = dice_prompt[modifierIndex:]
            if modifier_str[0] not in ('+', '-'):
                raise Exception("Modifier must start with '+' or '-'")
            if not modifier_str[1:].isdecimal():
                raise Exception("Modifier must be a number")
            modifier = int(modifier_str)
            
        rolls = []
        for i in range(num_dice):
            rolls.append(random.randint(1, num_sides))
        
        print(f"Rolling {num_dice}d{num_sides}{'+' if modifier >= 0 else ''}{modifier}:")
        print(", ".join(str(roll) for roll in rolls))
        total = sum(rolls)
        if modifier != 0:
            print(f"{total} {'+' if modifier > 0 else '-'} {abs(modifier)}", end='')
        total += modifier
        print(f" = {total}")

    except Exception as e:
        print(f"Invalid input! {e}")
        continue

        
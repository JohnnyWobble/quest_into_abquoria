import things
import random as rd

total_wager = 0


def rulesForDice():
    print("Do you know the rules? [Y/N]")
    command = input("> ").upper()
    while True:
        if command in ["N", "NAH", "NO"]:
            print(
                "The goal of the game is to get a higher total number on your 3 dice then the traveler. Both you and the traveler have 3 dice, a 5 sided one, a 9 sided one and a 14 sided one, you each bet, then roll the 5 sided die, and repeat for the 9 and 14 sided die, if the traveler bets, you can match, fold, or raise, if he does not bet you can either bet or stay. ")
            input("[ENTER] to continue")
            return
        elif command in ["Y", "YEAH", "YES"]:
            return


def bettingStart():
    global dice_values
    global total_wager
    global player_total
    global comp_total
    print("Once you start you can't stop until you win lose or fold, do you want to conintue? [Y/N]")
    while True:
        command = input("> ").upper()
        if command in ["Y", "YEAH", "YES"]:
            break
        elif command in ["N", "NAH", "NO"]:
            return
    rulesForDice()
    if things.gold == 0:
        print("you have 0 gold, your broke, ya can't bet 0, it dont work like that")
        return
    a = betting(1, 0)
    total_wager = a
    comp_total = 0
    player_total = 0
    if a == True:
        return
    for i in [5, 9, 14]:
        dice_values = diceRoll(i)
        player_total += dice_values[0]
        comp_total += dice_values[1]
        print(f"you rolled a {dice_values[0]} and the traveller rolled a {dice_values[1]}")
        if i == 14:
            break
        a = betting(2, 0)
        if a != False:
            total_wager += a
        comp_des = logic(i, total_wager)
        if comp_des == 0:
            print("the traveller decided to match you")
            continue
        else:
            a = betting(3, comp_des)
            if a == "LEAVE":
                return
    print(f"You rolled a total of {player_total} and the traveller rolled a total of {comp_total}")
    if player_total > comp_total:
        print(f"Congrats, you won {total_wager} more gold")
        things.gold += 2 * total_wager
    elif comp_total > player_total:
        print(f"Wow, you managed to loose {total_wager} gold, good job")
    else:
        print(f"So, you both tied and each got {total_wager} gold, you broke even")
        things.gold += total_wager
    return


def logic(d_type, player_wager):
    ratios = {5: 2, 9: 4}
    if dice_values[1] - dice_values[0] >= ratios.get(d_type):
        comp_wager = int(player_wager * 0.2)
        if comp_wager == 0:
            comp_wager == 1
        if comp_wager < things.gold:
            comp_wager -= comp_wager - things.gold
        elif things.gold == 0:
            comp_wager = 0
        return comp_wager
    return 0


def wagerAmount(comp_wager, comp_raise, round_number):
    if things.gold <= 0:
        print("Dang you broke, no more betting for you")
        return False
    if round_number == 2:
        print("Do you want to bet (b) more or stay (s)?")
        while True:
            command = input("> ").upper()
            if command in ["BET", "B"]:
                break
            elif command in ["STAY", "S"]:
                return 0
    elif round_number == 3:
        print("Do you want to raise (r), stay (s), or fold (f)")
        while True:
            command2 = input("> ").upper()
            if command2 in ["Raise", "R"]:
                break
            elif command2 in ["STAY", "S"]:
                print(f"You matched the traveler at {comp_wager} gold")
                print(f"You now have {things.gold} gold")
                return comp_wager
            elif command2 in ["FOLD", "F"]:
                return "LEAVE"
    while True:
        breaker = False
        print(f"How much do you want to bet? You have {things.gold} gold")
        while True:
            try_wager = input("> ")
            try:
                try_wager = int(try_wager)
            except:
                continue
            if try_wager + comp_wager > things.gold or try_wager <= 0:
                continue
            else:
                if comp_raise:
                    print(f"Are you sure you want to wager {try_wager} in addition to the {comp_raise}")
                print(f"Are you sure you want to wager {try_wager} gold? [Y/N]")
                while True:
                    confirm = input(">> ").upper()
                    if confirm in ["N", "NO"]:
                        breaker = True
                        break
                    elif confirm in ["Y", "YES", "YEAH"]:
                        try_wager += comp_wager
                        things.gold -= try_wager
                        return try_wager
            if breaker:
                break
        if breaker:
            continue


def betting(round_number, comp_wager):
    if round_number in [1, 2]:
        return wagerAmount(comp_wager, False, round_number)
    elif round_number == 3:
        return wagerAmount(comp_wager, True, 3)


def diceRoll(number_of_sides):
    input(f"\n[ENTER] to roll the {number_of_sides} sided die")
    return [rd.randint(1, number_of_sides), rd.randint(1, number_of_sides)]


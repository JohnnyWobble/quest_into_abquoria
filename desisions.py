import fights
import random as rd
import things
from obituary import spaceAdder
import dice

sell_list = []
sell_price_list = []
traveler_count = 0


def desList():
    global traveler_count
    while True:
        a = rd.randint(1, 100)
        if a < 50:
            fights.fightChance(fights.level)
            traveler_count = 0
        elif 80 > a >= 50:
            leftright()
        elif a >= 80 and traveler_count < 2:
            traveler_count += 1
            otherPerson()


def findItem():
    for i in [0, 1, 2, 3]:
        print("hi")


def test():
    print("test1")


def fightsy():
    print("works")


def Decide():
    global traveler_count
    while True:
        h = rd.randint(0, 4)
        if h != 0:
            traveler_count = 0
            fights.fightChance(fights.level)
        elif traveler_count < 2:
            traveler_count += 1
            otherPerson()


def leftright():
    decide = input("left (l) or right (r)? ").upper()
    while True:
        if decide in ["LEFT", "L"]:
            Decide()
            return
        elif decide in ["RIGHT", "R"]:
            Decide()
            return
        else:
            print("Bruh, just pick")
            decide = input("left or right? ").upper()


def otherPerson():
    global sell_list
    global sell_price_list
    sell_list.clear()
    sell_price_list.clear()
    print(
        "\nyou met another traveler who was trying to escape the evil tyrant in \nPyhras, and he has some items that he is willing to sell\n[ENTER] to continue")
    input("> ")
    for i in range(rd.randint(1, 5)):
        sell_list.append(rd.choice(things.buyable_items))
        sell_price_list.append(
            rd.randint(int((sell_list[i].value) - ((sell_list[i].value) * fights.range_of_variation)),
                       int((sell_list[i].value) + ((sell_list[i].value) * fights.range_of_variation))))
    while True:
        print(f"you have {things.gold} gold")
        print("Item:               Price:")
        for i in range(len(sell_list)):
            print(f"  {i + 1}) {spaceAdder(sell_list[i].name, 20)}{sell_price_list[i]}")
        print("\nActions:")
        print('  inventory (i)\n  gamble (g)\n  leave (l)')
        print("\nWhat do you want?")
        breaker = False
        command = input("> ").upper()
        while True:
            if command.upper() in ['LEAVE', 'L']:
                return
            if command.upper() in ['I', 'INVENTORY']:
                fights.inventory()
                breaker = True
                break
            if command.upper() in ["GAMBLE", "G"]:
                dice.bettingStart()
                breaker = True
                break
            try:
                command = int(command)
            except:
                command = input(">> ")
                continue
            if command in list(range(1, len(sell_list) + 1)):
                break
            command = input("> ")
        if breaker:
            breaker = False
            continue
        print(f"are you sure you want to buy the {sell_list[command - 1].name} for {sell_price_list[command - 1]} gold? [Y/N]")
        while True:
            command2 = input(">> ").upper()
            if command2 in ['YES', 'Y', 'YEAH']:
                if things.gold - sell_price_list[command - 1] < 0:
                    print("you don't have enought gold for this purchase")
                    break
                else:
                    things.gold -= sell_price_list[command - 1]
                    if sell_list[command - 1].otype == 'health':
                        things.inventory.append(sell_list[command - 1])
                        sell_list.pop(command - 1)
                        sell_price_list.pop(command - 1)
                        break
                    elif sell_list[command - 1].otype == 'weapon':
                        things.weapon_list.append(sell_list[command - 1])
                        things.weapon_health_list.append(sell_list[command - 1].health)
                        sell_list.pop(command - 1)
                        sell_price_list.pop(command - 1)
                        break
                    elif sell_list[command - 1].otype == 'armor':
                        if sell_list[command - 1] in things.armor_list:
                            print(f"bruh you can wear two {sell_list[command - 1].name}s, it don't work like that")
                            things.gold += sell_price_list[command - 1]
                            break
                        things.armor_list.append(sell_list[command - 1])
                        sell_list.pop(command - 1)
                        sell_price_list.pop(command - 1)
                        break
            elif command2 in ['N', 'No', 'NAH']:
                break
        continue


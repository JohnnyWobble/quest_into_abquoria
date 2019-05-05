# Sorry about the readibility, I am working on developing the program ASAP so readibilty is not a priority, I will work on readability after the game jam ends

import things
import random as rd
import obituary
import secret
import winner
from obituary import spaceAdder

player_name = ''
mob_kill_count = 0
mob_kills_to_levelup = 8
level = 1


diffe = ({1:(20, 5, 0, 0, 0), 2:(15, 10, 2, 0, 0), 3:(10, 15, 7, 1, 0), 4:(6, 13, 13, 5, 0), 5:(3, 8, 12, 10, 0), 6:(0, 0, 0, 0, 1)}) # this is the rarity count for weapons, the key is the rarity and the tuple are the odds of them 'spawning'
range_of_variation = 0.2


def fightChance(level): # this determines what level monster you fight
  sett = {}
  woup = []
  for i in (0, 1, 2, 3, 4):
    sett.update({diffe.get(level)[i]:i})
    diffe.get(level)[i]
    a = diffe.get(level)[i]
    for j in range(a):
      sett.get(a)
      woup.append(sett.get(a))
  b = rd.choice(woup)
  if fight(b) == 1:
    return 1

def fight(chance): # this is the main menu
  global mob_health
  global mob_dam
  global mob_de
  wank_dawg = False
  z = rd.choice(things.monsterList[chance])
  mob_health = rd.randint(int(z.health-(z.health*range_of_variation)), int((z.health+(z.health*range_of_variation)))) #this randomizes the health of the monster within a plus minus range of 20%
  mob_dam = z.attack
  mob_de = z.defense
  a = z.name
  print(f"\nYou have stumbled accross a {a}!")
  print(f"the {a} has {mob_health}hp")
  print(f"\nyour health is at {things.health}hp")
  while True:
    # print(f"kills: {mob_kill_count}, level: {level}")
    print("Options:\n   fight (f)\n   run (r)\n   inventory (i)\n   use item (u)")# prints menu
    command = input("> ").upper()
    while command not in ["RUN", "USE ITEM", "FIGHT", "INVENTORY", "U", "USE", "R", "F", "I"]: # checks to make sure it is a valid command
      if secret.EasterEggChecker(command):
        wank_dawg = True
        break
      command = input("> ").upper() # Repeats prompt
    if wank_dawg:
      wank_dawg = False
      continue
    if command in ['RUN', 'R']:
      a = rd.randint(1, 4)
      if a == 4:
        nopp = 1
        for i in range(len(things.armor_list)):
          nopp += ((things.armor_list)[i].defense)-1
        att = rd.randint(z.attack-(z.attack*range_of_variation), (z.attack+(z.attack*range_of_variation)))
        att = int((att // nopp) // 2)
        things.health -= att
        if things.health > 0:
          print(f"\nas you ran away {z.name} cliped you with its attack and did {att} damage to you, leaving you at {things.health}hp\n")
        else:
          print("wow, you died running away")
          obituary.obituary(player_name)
      else:
        print(f"you managed to run fast enough to evade the {z.name}")
      return 1
    elif command in ['USE', 'U', 'USE ITEM']:
      print("what do you want to use?")
      print(f"you are at {things.health}hp")
      print("options:     effect:")
      for i in range(len(things.inventory)):
        print(f"   {spaceAdder((things.inventory)[i].name, 12)}+{(things.inventory)[i].hadd}hp")
      print('back')
      c = finditem()
      if not c or c == 4:
        continue
      continue
    elif command in ['INVENTORY', 'I']:
      inventory()
      continue
    elif command in ['FIGHT', 'F']:
      d = mobSet(z)
      if not d:
        continue
      if d == 1:
        return 1

def inventory():
  print("you have:\n")
  print(" Gold:")
  print(f"   {things.gold} gold\n")
  print(" Weapons:")
  for i in range(len(things.weapon_list)):
    if i == 0:
      print(f"   {list(things.weapon_list)[i].name}    infinite")
    else:
      print(f"   {list(things.weapon_list)[i].name}    {list(things.weapon_health_list)[i]}hp")
  print("\n Other Items:")
  for i in range(len(things.inventory)):
    print(f"   {spaceAdder((things.inventory)[i].name, 12)}+{(things.inventory)[i].hadd}hp")
  print("\n Armor:")
  memes = 1
  for i in range(len(things.armor_list)):
    memes += (things.armor_list)[i].defense-1
  for i in range(len(things.armor_list)):
    print(f"   {spaceAdder((things.armor_list)[i].name, 20)}{int((((things.armor_list)[i].defense - 1)/(memes - 1))*int(100 - 100//(memes)))}%")
  print(f"  total:              -{int(100 - 100//(memes))}% of damage")
  print('\n[ENTER] to go back')
  input('>> ')

def finditem():
  while True:
    command3 = input(">> ").upper()
    for i in range(len(things.inventory)):
      if command3 == (things.inventory)[i].name.upper():
        a = useitem(things.inventory[i])
        if a == 1:
          return False
        elif a == 2 or a == 3:
          print(f'your health is now at {things.health}hp')
          return 4
    if command3 == 'BACK':
      return 5

def useitem(a):
  if things.health == 100:
    print('You are already at 100hp')
    return 1
  elif things.health + a.hadd > 100:
    things.health = 100
    things.inventory.remove(a)
    return 2
  else:
    things.health += a.hadd
    things.inventory.remove(a)
    return 3

def mobSet(name):
  while True:
    print("What weapon will you use?\nOptions:  Health:   Damage (c):     Damage (r):")
    for i in range(len(things.weapon_list)):
      if i == 0:
        uno = int(int((things.weapon_list)[i].attack1-(things.weapon_list)[i].attack1*range_of_variation)*name.defense)
        dous = int(int((things.weapon_list)[i].attack1+(things.weapon_list)[i].attack1*range_of_variation)*name.defense)
        tres = int(int((things.weapon_list)[i].attack2-(things.weapon_list)[i].attack2*range_of_variation)*name.defense)
        quatro = int(int((things.weapon_list)[i].attack2+(things.weapon_list)[i].attack2*range_of_variation)*name.defense)
        a = spaceAdder(f"{uno}-{dous} damage", 16)
        b = spaceAdder(f"{tres}-{quatro} damage", 16)
        print(f"   {i+1}) {things.fist.name}     ∞hp    {a}{b}")
      else:
        uno = int(int((things.weapon_list)[i].attack1-(things.weapon_list)[i].attack1*range_of_variation)*name.defense)
        dous = int(int((things.weapon_list)[i].attack1+(things.weapon_list)[i].attack1*range_of_variation)*name.defense)
        tres = int(int((things.weapon_list)[i].attack2-(things.weapon_list)[i].attack2*range_of_variation)*name.defense)
        quatro = int(int((things.weapon_list)[i].attack2+(things.weapon_list)[i].attack2*range_of_variation)*name.defense)
        a = spaceAdder(f"{uno}-{dous} damage", 16)
        b = spaceAdder(f"{tres}-{quatro} damage", 16)
        print(f"   {i+1}) {spaceAdder((things.weapon_list)[i].name, 8)} {(things.weapon_health_list)[i]}hp    {a}{b}")
    print(" back")
    a = input(">> ")
    while True:
      if a.upper() in ['BACK', 'NOTHING', 'NO']:
        return
      try:
        a = int(a)
      except:
        a = input(">> ")
        continue
      if a in list(range(1, len(things.weapon_list)+1)):
        break
      a = input(">> ")
    b = list(things.weapon_list)[a-1]
    if mobFight(name, b, a-1) == 1:
      return 1
    else:
      continue
    break
    if a == 'BACK':
      return False
    break

def mobFight(monster, weapon, indexy):
  global range_attack_boolean
  global mob_health
  global mob_dam
  global mob_de
  counter = 0
  while True:
    if counter >= 1:
      print("Same attack again? [Y/N]")
      while True:
        b = input(">>>> ").upper()
        if b in ['No', 'N']:
          return
        if b in ['YES', 'Y']:
          break
    else:
      print("Ranged (r) attack or close (c) attack or back?")
    while True:
      if counter < 1:
        a = input(">>> ").upper()
      if a not in ['RANGED', 'R', 'CLOSE', 'C', 'BACK', 'NO']:
        continue
      elif a in ['RANGED', 'R']:
        if weapon.attack2 == 0:
          print(f"A {weapon.name} is not capable of a ranged attack, use it in a close \nattack instead")
          continue
        else:
          weap_d = rd.randint(int(weapon.attack2-(weapon.attack2*range_of_variation)), int((weapon.attack2+(weapon.attack2*range_of_variation))))
          range_attack_boolean = True
          break
      elif a in ['CLOSE', 'C']:
        weap_d = rd.randint(int(weapon.attack1-(weapon.attack1*range_of_variation)), int((weapon.attack1+(weapon.attack1*range_of_variation))))
        range_attack_boolean = False
        break
      elif a in ['BACK', 'NO']:
        return
    print(f"you attacked a {monster.name} with a {weapon.name}")
    dam = int(weap_d*monster.defense)
    mob_health -= dam
    mob_de -= mob_de*weapon.denock
    if mob_health <= 0:
      mob_health = 0
      print(f"you have vanquished the {monster.name} with a {weapon.name}")
      things.gold += loot(level, monster)
      global mob_kill_count
      things.points += monster.point_value
      mob_kill_count += 1
      levelUpCheck()
      checkWeaponBreak(indexy, range_attack_boolean)
      return 1
    else:
      print(f"\nyou did {dam} damage to the {monster.name}, and it is now at {mob_health}hp")
    counter += 1
    if monAttack(monster):
      print(f"Well {player_name} ... You died, and failed your people")
      obituary.obituary(player_name)
    if checkWeaponBreak(indexy, range_attack_boolean):
      return

def checkWeaponBreak(indexy, range_attack_boolean):
  if range_attack_boolean:
    things.weapon_health_list[indexy] -= 2
  else:
    things.weapon_health_list[indexy] -= 1
  if things.weapon_health_list[indexy] <= 0:
    print(f"your {things.weapon_list[indexy].name} broke\n")
    things.weapon_list.pop(indexy)
    things.weapon_health_list.pop(indexy)
    return True
  else:
    return False

def levelUpCheck():
  global mob_kill_count
  global level
  if mob_kill_count >= mob_kills_to_levelup:
    mob_kill_count = 0
    level += 1
    levelUp()
    return

def levelUp():
  if level == 2:
    print("\nYou managed to find a crack in one of the walls large enough to slip through, and on the other side of the wall it is colder, darker, and more ancient\n")
    input("[ENTER] to continue")
    return
  elif level == 3:
    print("\nyou found a trap door and climbed down the ladder under the trapdoor, after a few feet you started to feel chilled to the bone and something inside of you just wanted to bolt outta here\n")
    input("[ENTER] to continue")
  elif level == 4:
    print("\nin the floor there was a massive crater that looked like it was made by an exposion of sorts, at the bottem of the crater there was ice, and as you picked your way down you slipped and hurt your knee and took 10 damage")
    things.health -= 10
    if things.health <= 0:
      input("\n[ENTER] to continue")
      print("\nyou died to a fall, wow")
      obituary.obituary(player_name)
    else:
      print("but at the bottem you saw more tunnels, so you continued exploring")
      input("\n[ENTER] to continue")
      return
  elif level == 5:
    print("\nyou see a doorway carved straight into the side of the tunnel, it was dark on the other side and ice covered the doorway, you know innately that if you could get through these new tunnels you would find a way out and could then save your people\n")
    input("[ENTER] to continue")
    return
  elif level == 6:
    print("there is no running now, you see light up ahead, but when you get closer \nyou find yourself in a rotunda full of exits and more paths which \nprobably contained more blast ended skrewts, but each one was protected \nby a blast ended skrewt, and you had to fight one to get out\n")
    input("[ENTER] to continue")

def monAttack(monster):
  nopp = 1
  for i in range(len(things.armor_list)):
    nopp += ((things.armor_list)[i].defense)-1
  att = rd.randint(monster.attack-(monster.attack*range_of_variation), monster.attack+(monster.attack*range_of_variation))
  att = int(att // nopp)
  things.health = int(things.health - att)
  if things.health > 0:
    print(f"\nthe {monster.name} did {att} damage to you, leaving you at {things.health}hp\n")
  else:
    return True

def loot(level, monster):
  oops = rd.randint(1*level, 5*level)
  if monster == things.dragon:
    oops = oops*5
  elif monster == things.blast_ended_skrewt:
    winner.winner()
  if rd.randint(1, 3) == 1:
    opps = get_weapon()
    print(f"after looting the {monster.name} you found {oops} gold and a {opps.name}")
  else:
    print(f"you found {oops} gold after looting the body of the {monster.name}")
    print("[ENTER] to continue")
    input("> ")
  return oops

def get_weapon():
  wouf = [3, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
  oof = things.wrarity[rd.choice(wouf)][rd.randint(0, 1)]
  things.weapon_list.append(oof)
  things.weapon_health_list.append(oof.health)
  return oof
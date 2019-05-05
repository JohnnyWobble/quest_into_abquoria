class monsters:
  def __init__(monster, otype, name, health, defense, attack, hardness, point_value):
    monster.name = name
    monster.otype = otype
    monster.health = health
    monster.defense = defense
    monster.attack = attack
    monster.hardness = hardness
    monster.point_value = point_value

class weapons:
  def __init__(weapon, otype, name, health, attack1, attack2, denock, rarity, value):
    weapon.name = name
    weapon.health = health
    weapon.otype = otype
    weapon.attack1 = attack1
    weapon.attack2 = attack2
    weapon.denock = denock
    weapon.rarity = rarity
    weapon.value = value

class healthItems:
  def __init__(item, otype, name, hadd, rarity, value):
    item.otype = otype
    item.name = name
    item.hadd = hadd
    item.rarity = rarity
    item.value = value

class armor:
  def __init__(armor, otype, name, defense, value):
    armor.otype = otype
    armor.name = name
    armor.defense = defense
    armor.value = value

# monster objects
urgal = monsters('monster', 'urgal', 50, 1, 50, 2, 80)
zombie = monsters('monster','zombie', 60, 2, 40, 2, 55)
ghost = monsters('monster','ghost', 30, 0.65, 15, 1, 40)
ogre = monsters('monster','ogre', 50, 0.5, 60, 3, 110)
troll = monsters('monster','troll', 60, 0.5, 70, 3, 125)
thief = monsters('monster','thief', 40, 1.25, 30, 1, 35)
witch = monsters('monster','witch', 50, 0.60, 30, 2, 70)
big_rat = monsters('monster','big rat', 30, 1, 10, 1, 15)
skeleton = monsters('monster','skeleton', 40, 1, 20, 1, 40)
dragon = monsters('monster','dragon', 90, 0.4, 100, 4, 170)
blast_ended_skrewt = monsters('monster','blast ended skrewt', 200, 0.25, 200, 5, 250)
test = monsters('monster', 'test', 100, 1, 100, 6, 100)

points = 0

monsterList = [[ghost, thief, big_rat, skeleton], [urgal, zombie, witch], [ogre, troll], [dragon], [blast_ended_skrewt], [test]]

# weapon objects
fist = weapons('weapon', 'fist', 999999999, 10, 0, 0.05, 0, 0)
knife = weapons('weapon', 'knife', 20, 20, 35, 0.1, 2, 10)
stick = weapons('weapon', 'stick', 10, 15, 20, 0.2, 1, 2)
axe = weapons('weapon', 'axe', 25, 70, 0, 0.3, 3, 40)
sword = weapons('weapon', 'sword', 20, 40, 0, 0.25, 3, 30)
hammer = weapons('weapon', 'hammer', 30, 60, 0, 0.35, 2, 28)
flail = weapons('weapon', 'flail', 25, 75, 0, 0.2, 4, 45)
wand = weapons('weapon', 'wand', 20, 30, 60, 0.3, 4, 28)
rock = weapons('weapon', 'rock', 10, 20, 30, 0.05, 1, 3)

wrarity = [[stick, rock], [knife, sword], [wand, hammer], [flail, axe]]

weapon_list = [fist]
weapon_health_list = [fist.health]

#health item objects
pill = healthItems('health', 'pill', 50, 3, 12)
chugjug = healthItems('health', 'chugjug', 100, 4, 20)
band_aid = healthItems('health', 'band-aid', 20, 1, 3)
advil = healthItems('health', 'advil', 30, 1, 6)
gauze = healthItems('health', 'gauze', 40, 2, 7)

inventory = [band_aid, band_aid]
gold = 0


health = 100
big_inv = [weapon_list, inventory]

# armor objects
leather_jacket = armor('armor', 'leather jacket', 1.25, 12)
chainmail = armor('armor', 'chainmail', 1.3, 14)
hard_hat = armor('armor', 'hard hat', 1.3, 15)
iron_scale = armor('armor', 'iron scale armor', 2, 22)
boots = armor('armor', 'boots', 1.1, 10)
safety_glasses = armor('armor', 'safety glasses', 5, 45)
kevlar = armor('armor', 'kevlar', 3, 35)

armor_list = []

arrarity = [[leather_jacket, hard_hat, boots], [chainmail, iron_scale], [kevlar], [safety_glasses]]

buyable_items = [knife, stick, axe, sword, hammer, flail, wand, rock, pill, chugjug, band_aid, advil, gauze, leather_jacket, chainmail, hard_hat, iron_scale, boots, safety_glasses, kevlar]

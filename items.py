#Weapons
class Weapon:
    def __init__(self):
        raise NotImplementedError("Don't create raw weapon objects.")
    def __str__(self):
        return self.name
class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist size rock, Good for smashing things."
        self.damage = 5
        self.value = 1
class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust on it; somewhat more dangerous thana rock"
        self.damage = 10
        self.value = 20
class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "An aged sword with visible rust on it; but it still have some fight left in it"
        self.damage = 20
        self.value = 100
class BroadSword(Weapon):
    def __init__(self):
        self.name = "Broad sword"
        self.description = "A normal sword, nothing special about it except that it is still sharp"
        self.damage = 25
        self.value = 220
class BattleAxe(Weapon):
    def __init__(self):
        self.name = "Battle axe"
        self.description = "A double edged battle axe, suitable for ripping flesh and bone alike"
        self.damage = 30
        self.value =500
class NadersShamshir(Weapon):
    def __init__(self):
        self.name = "The Shamshir of Nader"
        self.description = "The legendry sword of the conqueror king of persia, Nader shah the great. still sharp as the" \
                           "day Nader conquered india with it."
        self.damage = 85
        self.value = 900
class BowOfArash(Weapon):
    def __init__(self):
        self.name = "Bow of Arash"
        self.description = "Bow of legendry persian archer; Arash'e Kamangir." \
                           "Arash grew persias borders shooting an arrow from this bow" \
                           "it is said that if your have the power draw this bow, nothing will stop your shot" \
                           "from reaching it's target."
        self.damage = 45
        self.value = 80
    #Consumables

# Consumables
class Consumable:
    def __init__(self):
        raise NotImplementedError("Do now creat raw consumable item.")
    def __str__(self):
        return self.name
class CrustyBread(Consumable):
    def __init__(self):
        self.name = 'Crusty bread'
        self.healing_value = 10
        self.value = 5
class HealingPotion(Consumable):
    def __init__(self):
        self.name = 'Healing potion'
        self.healing_value = 30
        self.value = 50
class LargeHealingPotion(Consumable):
    def __init__(self):
        self.name = 'LargeHealingPotion'
        self.healing_value = 100
        self.value = 90

# Valuables(Iems you can sell to trader)
class Valuable:
    def __init__(self):
        raise NotImplementedError("Don't make raw valuable object.")
    def __str__(self):
        return self.name
class GemStone(Valuable):
    def __init__(self):
        self.name = "Gem stone"
        self.description = "A big shiny gem, looks valuable."
        self.value = 200
class GoldBar(Valuable):
    def __init__(self):
        self.name = "Gold bar"
        self.description = "A big bar of gold, maybe someone will pay a good price for it."
        self.value = 150
class Diamond(Valuable):
    def __init__(self):
        self.name = "Diamond"
        self.description = "A big beautiful rock, so beautiful that it may be addictive to even look at."
        self.value = 500
class GoldRing(Valuable):
    def __init__(self):
        self.name = "Golden ring"
        self.description = "An old jewl belonging to an unknown person, look like a wedding ring; after all the  this time you can still" \
                           "say it will fetch a good price"
        self.value = 90

import random
import enemies
import npc
import items

class Maptile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass
class StartTile(Maptile):
    def intro_text(self):
        return ''' 
        You find yourself in a dark unfamilliar dungeon, you can barely see but as time passes your eyes
        adjust to the darkness, your only hope is to find a way out from this creepy place.
        '''
class EnemyTile(Maptile):
    def __init__(self, x,y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text = "A giant spider jumps down from it's web in front of you! blocking your path"
            self.dead_text = "Corpes of a dead spider rots the ground"
        elif r < 0.80:
            self.enemy = enemies.BatColony()
            self.alive_text = "You hear a sqeaking sound,it grows louder by the second" \
                              "suddenly you find yourself lost in a bat swarm"
            self.dead_text = "Dozens of dead bats rot the ground..."
        elif r < 0.95:
            self.enemy = enemies.Div()
            self.alive_text = "A big brown div appears in frnt of you out of nowhere!"
            self.dead_text = "The giant div corpes remind you of your triumph"
        else:
            self.enemy = enemies.BlackDiv()
            self.alive_text = "You hear growling from the corner of the room...\n" \
                              "Before you can notice anything you see a giant black div in front of you\n" \
                              "smoke coming out of his mouth; fire burning in its eyes...prepare for pain."
            self.dead_text = "As you gaze uppon the dead black div; you are reminded once again how strong you can be."
        super().__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("{} does {} damage. You have {} HP remaining".
                  format(self.enemy.name, self.enemy.damage, player.hp))
    def intro_text(self):
        if self.enemy.is_alive():
            text = self.alive_text
        else:
            text = self.dead_text
        return text
class BoringTile(Maptile):
    def intro_text(self):
        return ''' There is not much to be done or seen
        here..
        '''
class FindGoldTile(Maptile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)
    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold += self.gold
            print("+{} Gold added.".format(self.gold))
        else:
            return "Someone dropped some gold, pick it up"
    def intro_text(self):
        return f"You see a closed box in fron of you; it seem someone forgot to lock it."
class VictoryTile(Maptile):
    def intro_text(self):
        return '''You see a bright light at the end of the tunnel;
        you feel the wamth,... it's... Sunlight.
        === VICTORY ===
        '''
class TraderTile(Maptile):
    def __init__(self,x,y):
        self.trader = npc.Trader()
        super().__init__(x,y)
    def intro_text(self):
        return """
        Afrail not quite human, not quiet beast squats in the corne;
        clinking his gold coins together.He looks willing to trade.
        """
class TreasureTile(Maptile):
    def __init__(self, x, y):
        self.item_claimed = False
        t = random.random()
        box_weapons = [items.BattleAxe(), items.RustySword(), items.BowOfArash(), items.NadersShamshir(),
                       items.BroadSword()]
        box_consumables = [items.LargeHealingPotion(), items.HealingPotion()]
        box_valuables = [items.GoldBar(), items.Diamond(), items.GemStone()]
        def modify_player(self, player):
            if not self.item_claimed:
                self.item_claimed = True
                if t < 0.50:
                    treasure_item = random.choice(box_consumables)
                elif t < 0.70:
                    treasure_item = random.choice(box_weapons)
                else:
                    treasure_item = random.choice(box_valuables)
                print("{} added to your inventory".format(treasure_item))
                player.inventory.append(treasure_item)

def tile_at(x, y):
    if x < 0 or y <0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
world_dsl = """
|EN|EN|VT|EN|EN|
|EN|TB|  |TB|EN|
|EN|FG|EN|  |TT|
|TT|TB|ST|FG|EN|
|FG|  |EN|  |FG|
"""
world_map = []
def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True
tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "BT": BoringTile,
                  "TB": TreasureTile,
                  "  ": None}
def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is not valid")
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x,y) if tile_type else None)
        world_map.append(row)


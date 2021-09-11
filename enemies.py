class Enemy:
    def __init__(self):
        raise NotImplementedError ("Do not create raw enemy class objects.")
    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0
class Div(Enemy):
    def __init__(self):
        self.name = "Div"
        self.hp = 30
        self.damage = 10
class GiantSpider(Enemy):
    def __init__(self):
        self.name = 'Giant spider'
        self.hp = 10
        self.damage = 5
class BlackDiv(Enemy):
    def __init__(self):
        self.name = 'Black div'
        self.hp = 35
        self.damage = 20
class BatColony(Enemy):
    def __init__(self):
        self.name = 'Bat Colony'
        self.hp = 100
        self.damage = 5
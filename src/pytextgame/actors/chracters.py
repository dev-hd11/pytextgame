# (C) 2024 - present. Himank Deka. All rights reserved
class Player :
    def __init__(self, title: str, armoury: list, health: int, money: int) :
        self.title = title
        self.armoury = armoury
        self.health = health
        self.money = money
        self.x = 0
        self.y = 0
        self.status = None

    def use_item(self, args: list, item_name: str) :
        for item in self.armoury :
            if item.name == item_name :
                item.use(args, self)

    
class Enemy :
    def __init__(self, health: int, message_to_player: str = '') :
        self.health = health
        self.message_to_player = message_to_player

    def setDamage(self, damage) :
        self.damage = damage

    def dealDamage(self, player) :
        player.health -= self.damage
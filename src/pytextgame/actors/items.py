# (C) 2024 - present. Himank Deka. All rights reserved
class Item :
    def __init__(self, price: int, name: str, description: str) :
        self.price = price
        self.name = name
        self.description = description

    def can_buy(self, player) :
        return player.money >= self.price
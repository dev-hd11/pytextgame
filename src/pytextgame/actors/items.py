"""
This file contains classes for in-game items.
(c) Himank Deka & Contributers [See CONTRIBUTING.md], 2023.
All rights reserved.
"""

from pytextgame.actors.charecter import Charecter
from pytextgame.components.errors import NotUpgradableError
import random as r

class Item :
    def __init__(self, 
                 name: str, 
                 desc: str,
                 price: float, 
                 present_lv: bool = False, 
                 lv: int = 0, 
                 max_lv: int = 0, 
                 can_upgrade: bool = False,
                 upgrade_prices: dict = {0 : 0}
                 ) :
        self.name = name
        self.price = price
        if present_lv :
            self.lv = lv
            self.max_lv = max_lv
            self.can_upgrade = can_upgrade
            self.upgrade_prices = upgrade_prices
            
        else :
            pass
        
    def describe(self) :
        return f"{self.name} : {self.desc}"
    
    def search(self, dict: dict, target: any, key: bool = True) :
        if key :
            for key_in, _ in dict :
                if target == key_in :
                    return dict.get(key_in)
                else :
                    pass
                
            return None
        
        else :
            for key_in, value in dict :
                if value == target :
                    return key_in
                
                else :
                    pass
                
            return None
         
    
    def upgrade(self, other: Charecter) :
        if not self.can_upgrade :
            raise NotUpgradableError
        
        if self.lv == self.max_lv :
            return
        
        val = self.search(self.upgrade_prices, self.lv + 1) 
        money = other.withdraw(val)
        
        if money == None :
            return
        
        
        if val == None :
            return
        
        self.lv += 1
        
    def buy(self, other: Charecter) :
        val = self.price
        ifr = other.withdraw(val)
        
        if ifr == None :
            return
        
        else :
            other.items_in.append(self)
            

class Weapon(Item) :
    def __init__(self, 
                 name: str, 
                 desc: str,
                 price: float, 
                 random: bool,
                 damages: list[int] = [1],
                 present_lv: bool = False, 
                 lv: int = 0, 
                 max_lv: int = 0, 
                 can_upgrade: bool = False,
                 upgrade_prices: dict = {0 : {"ammo" : 0, "damage" : 0, "price" : 0, "range" : 0}},
                 damage: int = 1,
                 ammo: int = 1,
                 range: int = 0
            ) :
        
        super().__init__(name, desc, price, present_lv, lv, max_lv, can_upgrade, upgrade_prices)
        self.ammo = ammo
        self.range = range
        self.random = random
        if random :
            self.damages = damages
            
        else :
            self.damage = damage
        
    def describe(self) :
        super().describe()
        damage_str = f""
        if self.random :
            damage_str += f"Max damage: {max(self.damages)}\nMin damage: {min(self.damages)}"
            
        else :
            damage_str += f"Damage: {self.damage}"
            
        print(damage_str + f"\nRange: {self.range}\nAmmunition: {self.ammo}")
        
    def getDamage(self) :
        return self.damage
    
    def upgrade(self, other: Charecter) :
        if not super().can_upgrade :
            raise NotUpgradableError
        
        if super().lv == super().max_lv :
            return
        
        val = self.search(self.upgrade_prices, self.lv + 1) 
        val_p = val.get("price")
        money = other.withdraw(val_p)
        
        if money == None :
            return
        
        
        if val_p == None :
            return
        
        super().lv += 1
        self.damage += val.get("damage")
        self.ammo += val.get("ammo")
        self.range += val.get("range")
    
    def can_fire(self, dist: int) :
       if dist <= range and self.ammo > 0 :
           return True
        
       else :
           return False
        
    def fire(self, char: Charecter, armour_present: bool, armour: Armour = None) :
        if self.random :
            if armour_present :
                dmg = r.choice(self.damages)
                char.cur_health -= dmg - armour.protect()
                self.ammo -= 1
            
            else :
                dmg = r.choice(self.damages)
                char.cur_health -= dmg
                self.ammo -= 1
            
        else :
            if armour_present :
                char.cur_health -= self.damage - armour.protect()
                self.ammo -= 1
            else :
                char.cur_health -= self.damage
                self.ammo -= 1
            

        
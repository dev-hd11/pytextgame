"""
This file contains classes for all the charecters in the game
(c) Himank Deka & Contributers [See CONTRIBUTING.md], 2023.
All rights reserved.
"""

import pytextgame.actors.items as items

class Charecter :
    def __init__(self, 
                 name: str, 
                 desc: str, 
                 play: bool, 
                 weapon: items.Weapon, 
                 money: float = 0, 
                 health: float = 100, 
                 items_in: list[items.Item] = []
                 ) :
        self.name = name
        self.desc = desc
        self.play = play
        self.weapon = weapon
        self.health = health
        self.money = money
        self.balance = money
        self.cur_health = health
        self.items_in = items_in
        
    def showDesc(self) :
        print(f"{self.name} : {self.desc}")
        
    def dealDamage(self, other) :
        weapon = self.weapon
        other.takeDamage(weapon)
        
    def takeDamage(self, other_weapon: items.Weapon) :
        self.cur_health -= other_weapon.getDamage()
        
    def deposit(self, amount: int) :
        self.balance += amount
        
    def withdraw(self, amount: int) :
        if amount > self.balance :
            return None
        
        else :
            self.balance -= amount
            return amount
        
    
DEFAULT_WEAPON = items.Weapon(
    name = "fist",
    damage = 1,
    random = False,
    price = 0
)

class Hero (Charecter) :
    def __init__(self,name: str, 
                 desc: str, weapons: list[items.Weapon], 
                 portions: list[items.Portion],
                 money: float = 0,
                 health: float = 100,
                 armour = items.Armour, 
                 cur_weapon: items.Weapon = DEFAULT_WEAPON,
                 items_in: list[items.Item] = []
                 ) :
        super().__init__(name, desc, True, cur_weapon, money, health, items_in)
        self.weapons = weapons
        self.portions = portions
        self.armour = armour
        
    def changeWeapon(self, weapon: items.Weapon) :
        for i in self.weapons :
            if weapon.name == i.name :
                self.cur_weapon = weapon
                
            else :
                pass
            
    def usePortion(self, portion) :
        for i in self.portions :
            if portion.name == i.name :
                if self.cur_health == self.health :
                    pass
                
                elif self.cur_health < self.health and (self.cur_health + i.getRevival()) > self.health :
                    self.cur_health = self.health
                    
                else :
                    self.cur_health += i.getRevival()
                    
    def takeDamage(self, other_weapon: items.Weapon):
        damage = other_weapon.getDamage() - self.armour.protect()
        self.cur_health -= damage
        


"""
This file contains classes for in-game items.
(c) Himank Deka & Contributers [See CONTRIBUTING.md], 2023.
All rights reserved.
"""

from pytextgame.actors.charecter import Charecter
from pytextgame.components.errors import NotUpgradableError

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
            

        
        
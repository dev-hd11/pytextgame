"""
Copyright (c) 2023 Himank Deka & Contributers [See CONTRIBUTERS.txt]
"""
"""
This file contains the frames and the necessary components that will be displayed to the user.
"""

import os
import pytextgame.components.dat 

class Frame :
    def __init__(self, name, description, options) :
        self.name = name
        self.description = description
        self. options = options
        
    def clrscr() :
        os.system("cls")
        
    def show_frame(self) :
        self.clrscr()
        print(f"Title: {self.name}")
        print(f"{self.description}")
        for no, option in enumerate(self.options) :
            print(f"{no}. {option}")
            

    def process_opt(self, opt) :
        for i, _ in enumerate(self.options) :
            if i == opt :
                return self.options[i].script()
            
            else :
                return None
            
    def get_input(self) :
        opt = int(input(dat.INP_MSG))
        result = self.process_opt(opt)
        
        if result == None :
            print(dat.NOT_FOUND)
            
        else :
            return result
        
class Option :
    def __init__(self, name, verb) :
        self.name = name
        self.verb = verb
        
    def script(self) :
        return self.verb
    

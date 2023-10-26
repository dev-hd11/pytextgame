"""
Copyright (c) 2023 Himank Deka & Contributers [See CONTRIBUTERS.txt]
This file has components for creating rooms and all necessary components.
"""

from pytextgame.components.errors import *

class Door :
    def __init__(self, room, name, direction, lock: bool) :
        self.room = room
        self.name = name
        self.direction = direction
        self.lock = lock
        
    def change_lock(self) :
        self.lock = not self.lock
        
    def __str__(self) :
        return f"{self.name} in {self.room.name} on {self.room.play}"
        


class Room :
    def __init__(self, play, name, doors, objects, exit) :
        self.play = play
        self.doors = doors
        self.objects= objects
        self.name = name
        self.exit = exit
        
    def title(self) :
        return self.name
    
    def get_doors(self) :
        return self.doors
    
    def get_objs(self) :
        return self.objects
    
    def set_entry(self, prev_room) :
        entry = prev_room.get_exit()
        self.doors.append(Door(self, 'entry', entry, False))
        
    def get_exit(self) :
        if not exit :
            return None
        
        else :
            for door in self.doors :
                if door.title() == 'exit' :
                    return door.title()
                
                else :
                    err = ExitNotSetError()
                    print(err)
                    raise ExitNotSetError
                    
    def __str__(self) :
        return f"{self.name} on {self.play}"
                



        



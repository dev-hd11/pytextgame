# (C) 2024 - present. Himank Deka. All rights reserved

class Room :
    def __init__(
            self, 
            name: str, 
            objects: list, 
            room_scene, 
            exit_dirs: list, 
            enemy = None,
            exit_locked: bool = False
                 ) :
        self.name = name
        self.exit_locked = exit_locked
        self.room_scene = room_scene
        self.exit_dirs = exit_dirs
        self.enemy = enemy
        self.objects = objects

    def open_exit(self) :
        self.exit_locked = False

    def access(self, object_name: str) :
        for obj in self.objects :
            if obj.name == object_name :
                return obj
            
    def run(self, player) :
        self.room_scene.exec(player=player, room=self, enemy=self.enemy)

    def exit_room(self, player, direction: str) :
        direction = direction.lower()
        if direction not in self.exit_dirs :
            return 0
        
        elif direction == 'north' :
            player.x += 1

        elif direction == 'south' :
            player.x -= 1

        elif direction == 'west' :
            player.y += 1

        elif direction == 'east' :
            player.y -= 1
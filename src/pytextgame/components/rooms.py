# (C) 2024 - present. Himank Deka. All rights reserved
import pytextgame.components.scene as scene

class Room :
    def __init__(self, name: str, description: str, objects: list, room_scene: scene.Scene, exit_locked: bool = False) :
        self.name = name
        self.desc = description
        self.exit_locked = exit_locked
        self.room_scene = room_scene

    def open_exit(self) :
        self.exit_locked = False

    def access(self, object_name: str) :
        for obj in self.objects :
            if obj.name == object_name :
                return obj
            
    def run(self, player, enemy) :
        self.room_scene.exec(player, enemy, self)
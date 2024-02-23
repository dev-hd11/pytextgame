# (C) 2024 - present, Himank Deka. All rights reserved.
import numpy as np
import pytextgame.graphics.text as ascii
import pytextgame.components.rooms as rooms
import pytextgame.io as io

class Scene :
    def __init__(self, title: str, description: str, options: str) :
        self.title = title
        self.description = description
        options = np.array(options)

    def process(self, player, enemy, option: str, room: rooms.Room = None) :
        pass

    def exec(self, player, enemy, room: rooms.Room = None) :
        ascii.g_title(self.title, '', True)
        print(self.description)
        self.process(player, enemy, io.option_list(self.options))

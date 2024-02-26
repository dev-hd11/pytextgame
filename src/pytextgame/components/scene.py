# (C) 2024 - present, Himank Deka. All rights reserved.
import pytextgame.graphics.text as ascii
import pytextgame.components.rooms as rooms
import pytextgame.io as io

class Scene :
    def __init__(self, title: str, description: str, options: list) :
        self.title = title
        self.description = description
        self.options = options

    def process(self, player, option: str, room: rooms.Room = None, enemy = None) :
        pass

    def exec(self, player, room: rooms.Room = None, enemy = None) :
        ascii.clrscr()
        ascii.g_title(self.title, '', True)
        print(self.description)
        key = io.option_list(self.options)
        if key == None :
            self.exec(player, room, enemy)

        self.process(player, key, room, enemy)

class Screen :
    def __init__(self, title: str, description: str, options: list) :
        self.title = title
        self.description = description
        self.options = options

    def exec(self, process_function, args: list, clearscreen: bool = False) :
        if clearscreen :
            ascii.clrscr()

        ascii.g_title(self.title, '', True)
        print(self.description)
        key = io.option_list(self.options)
        if key == None :
            self.exec(process_function, args, True)

        process_function(args, key)
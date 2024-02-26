# (C) 2024 - present. Himank Deka. All rights reserved
import json
import pytextgame.graphics.text as ascii
import time
import sys

VERSION = '1.0'

class Playground :
    def __init__(self, settings_file_path: str, game_map: list, windows: bool = True) :
        self.sfp = settings_file_path
        self.data = dict()
        self.game_map = game_map

        ascii.clrscr()
        print(f"Built with PyTextGame v{VERSION}.\nCopyright (C) 2024 Himank Deka.\nGitHub: dev-hd11/pytextgame")

        for char in '-' * 22:
             sys.stdout.write(char)
             sys.stdout.flush()
             time.sleep(0.3)
    
        ascii.clrscr(windows)


    def importData(self, msg: bool = False) :
        try :
            with open(self.sfp, 'r') as jsonfile :
                    self.data = json.load(jsonfile)

                    if msg :
                        print("Imported settings!")

        except FileNotFoundError :
            print(f"{self.sfp} doesn't exist!")

        except json.JSONDecodeError as e :
            print(f"Error loading file: {e}")

    def setData(self, data: dict, msg: bool = False) :
        try :
            with open(self.spf, 'w') as jsonfile :
                json.dump(data, jsonfile)

                if msg :
                    print("Data set successfully!")
        except Exception as e :
            print(f"Error: {e}")

    def play(self, player) :
        while player.status is None :
            room = self.game_map[player.x][player.y]
            room.run(player)

            

        return player.status

# (C) 2024 - present. Himank Deka. All rights reserved
import json

class Playground :
    def __init__(self, settings_file_path: str) :
        self.sfp = settings_file_path
        self.data = dict()

    def set(self, msg: bool = False) :
        try :
            with open(self.sfp, 'r') as jsonfile :
                    self.data = json.load(jsonfile)

                    if msg :
                        print("Imported settings!")

        except FileNotFoundError :
            print(f"{self.sfp} doesn't exist!")

        except json.JSONDecodeError as e :
            print(f"Error loading file: {e}")

    



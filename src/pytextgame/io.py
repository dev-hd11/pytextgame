# (C) 2024 - present, Himank Deka. All rights reserved.
import numpy
import keyboard
import pytextgame.graphics.text as ascii
import time

def option_list(options: list, clearscreen: bool = False) :
    try :
        options = numpy.array(options)
        if clearscreen :
            ascii.clrscr()

        for i in range(options.size) :
            print(f"[{i + 1}] {options[i]}")

        key = getch()

        return options[int(key) - 1]
    
    except ValueError as e :
        print(f"Error: {e}")
        time.sleep(2)
        return option_list(options, True)

    except IndexError as e :
        print(f"Error: {e}")
        time.sleep(2)
        return option_list(options, True)

def getch():
    char = keyboard.read_event(suppress=True).name
    return char
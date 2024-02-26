# (C) 2024 - present, Himank Deka. All rights reserved.
import keyboard
import time

VERSION = '1.0'

def option_list(options: list) :
    try :
        for i in range(len(options)) :
            print(f"[{i + 1}] {options[i]}")

        key = int(input("Option:"))

        return options[int(key) - 1]
    
    except ValueError as e :
        print(f"Error: {e}")
        time.sleep(2)
        return None

    except IndexError as e :
        print(f"Error: {e}")
        time.sleep(2)
        return None

def getch():
    char = keyboard.read_event(suppress=True).name
    return char
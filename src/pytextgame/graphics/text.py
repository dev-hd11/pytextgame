# (C) 2024 - present, Himank Deka. All rights reserved.
import os

ENDL = '\n'

def g_title(txt: str, author: str, echo: bool = True) :
    decoration = "-" * 5 + "-" * len(txt) + "-" * 5 + ENDL
    title = decoration + " " * 5 + txt + " " * 5 + ENDL + decoration

    if echo :
        print(title + ENDL + "By " + author)

    else :
        return title + ENDL + "By " + author
    
def clrscr(windows: bool = True) :
    if windows :
        os.system('cls')

    else :
        os.system('clear')
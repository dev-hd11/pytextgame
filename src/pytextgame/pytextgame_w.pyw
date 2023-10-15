"""
File to display welcome message.
"""
"""
Copyright (c) 2023 Himank Deka & Contributers [See CONTRIBUTERS.txt]
"""

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import json as js


file = open("./settings.json", "r")
data = js.load(file)
file.close()
    

def main() :
    root = Tk()

    root.title("PyTextGame")
    root.geometry("800x600")

    greet = Label(
        root,
        text = "PyTextGame",
        font = ("Arial", 20),
        fg = "white",
        bg = "green",
    )
    

    greet.pack(pady = 10)


    img.pack(pady = 5)

    desc = Label(
        root,
        text = "Welcome to PyTextGame!\n Please visit https://www.github.com/dev-hd11/pytextgame/ for more information",
        font = ("Comic Sans MS", 15),
    )

    desc.pack(pady = 5)

    def close() :
        m = messagebox.askyesno(title = "PyTextGame", message = "Do you want to see this box again")
        if m:
            file2 = open("./settings.json", "w")
            data["show"] = "no"
            js.dump(data, file2)
            file.close()
        else :
            pass
        root.destroy()
    
    but = Button(
        root,
        text = "Let's Go!",
        font = ("Arial", 12),
        command = close,
        fg = "white",
        bg = "blue",
    )

    but.pack(pady = 5)
    
    lb1 = Label(
        root,
        text = "©️ Himank Deka and Contributers, 2023",
        fg = "gray",
    )
    
    lb1.place(x = 300, y = 500)
    
    root.mainloop()
    

if data.get("show") == "yes" :
    main()

else :
    pass
    

    
    

    
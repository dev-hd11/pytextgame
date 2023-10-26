"""
File to display welcome message.
Copyright (c) 2023 Himank Deka & Contributers [See CONTRIBUTERS.txt]
"""

from tkinter import *
from tkinter import messagebox




def main() :
    root = Tk()

    root.title("PyTextGame")
    root.geometry("800x400")

    greet = Label(
        root,
        text = "PyTextGame",
        font = ("Arial", 20),
        fg = "white",
        bg = "green",
    )
    

    greet.pack(pady = 10)


    desc = Label(
        root,
        text = "Welcome to PyTextGame!\n Please visit https://www.github.com/dev-hd11/pytextgame/ for more information",
        font = ("Comic Sans MS", 15),
    )

    desc.pack(pady = 5)

    def close() :
        m = messagebox.showwarning(title = "PyTextGame", message = "Pass the show_message_box arg as False in Playground().__init__()")
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
    

main()  

    
    

    
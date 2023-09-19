""" 
Here is the main file where the window is launched from.
"""
import customtkinter as ctk
from widgets_blueprints import (
    FontEntry,
    Root,
    CTkScrollableDropdown,
    TextBoxLabel,
    ChangeFontButton,
    TextBox,
)
from tkinter import font, Tk
tk = Tk()
# get all font available on pc owner
VALUES = list(font.families(tk,))
tk.destroy()

# set app's look  
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# create all 
root = Root()
font_entry = FontEntry(root)

# show a custom toplevel dropdown instead of the default dropdown-menu 
CTkScrollableDropdown(font_entry, values=VALUES,autocomplete=True, command=lambda e: font_entry.insert(0,e))
textbox_label = TextBoxLabel(root)
textbox = TextBox(root)
change_font_button = ChangeFontButton(root,textbox, font_entry)


# launch mainloop window
root.mainloop()  
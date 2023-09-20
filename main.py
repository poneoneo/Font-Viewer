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
    CurrentFontLabel
)

from tkinter import font, Tk
tk = Tk()
# get all font available on pc owner
VALUES = list(font.families(tk,))
tk.destroy()

# set app's look  
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

# create all 
root = Root()
font_entry = FontEntry(root)
textbox = TextBox(root)
textbox_label = TextBoxLabel(root,textbox)
current_font_label = CurrentFontLabel(root,textbox)
change_font_button = ChangeFontButton(root,textbox, font_entry,current_font_label)

# show a custom toplevel dropdown instead of the default dropdown-menu 
CTkScrollableDropdown(font_entry, values=VALUES,autocomplete=True, command=lambda e: font_entry.insert(0,e))

# launch mainloop window
root.mainloop()  
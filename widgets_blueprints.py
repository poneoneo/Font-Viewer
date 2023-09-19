""" 
Here is the building or blueprint file where we make design and setting all the
attributes, methodes, and behavior or all widgets in app
"""
from CTkScrollableDropdown import CTkScrollableDropdown
import customtkinter as ctk
import json



class Root(ctk.CTk):
    def __init__(self,):
        super().__init__()
        self.title("Show_Fonts_Effects")
        self.geometry("700x400")
        self.resizable(1,0)
        
        # set grid layout of root window app
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
      
class OptionMenu(ctk.CTkOptionMenu):
    def __init__(self, root):
        super().__init__(root,
                         variable=ctk.StringVar(value="Monotype Hadassah"),dropdown_font=ctk.CTkFont("Monotype Hadassah", 12, "bold"),width=100,)
        self.grid(column=1, row=1, )


class TextBoxLabel(ctk.CTkLabel):
    def __init__(self,root):
        super().__init__(root, text="Look at Your Font Effect Below", font=ctk.CTkFont("Mooli", 30, "bold"),corner_radius=0 )
        self.grid(column=0, row=0, pady=5 )
        
class FontEntry(ctk.CTkEntry):
    def __init__(self,root):
        super().__init__(root, text_color="white",font=ctk.CTkFont("Mooli", 10, "bold"),placeholder_text="Choose your font here" )
        self.grid(column=1, row=1,)
        self.bind("<Motion>", lambda e:self.border_blue(e))
        self.bind("<Leave>", lambda e:self.reset_default_border_color(e))
    def border_blue(self,event):
        self.configure(border_color="blue")
         
    def reset_default_border_color(self, event):
        self.configure(border_color="gray65") 
     
class TextBox(ctk.CTkTextbox):
    def __init__(self,root):
        super().__init__(root,corner_radius=12, fg_color="white", text_color="#171717",font=ctk.CTkFont("Mooli", 25, "bold") )
        self.grid(column=0, row=1, rowspan=3, sticky="ew", padx=10)
        self.bind("<FocusIn>",lambda e:self.border_blue(e))
        
    def border_blue(self,event):
        self.configure(border_color="blue") 
        self.update()

class ChangeFontButton(ctk.CTkButton):
    def __init__(self, root, textbox:TextBoxLabel, font_entry:FontEntry,**kwargs):
        super().__init__(root,text="Change", font=ctk.CTkFont("Mooli", 10, "bold"),**kwargs)
        self.configure(command=self.change_font)
        self.grid(column=1, row=2,)
        self.font_entry = font_entry
        self.textbox = textbox
        
    def change_font(self,):
        font_entry_value = self.font_entry.get()
        self.font_entry.delete(0,  ctk.END)
        self.textbox.configure(font=ctk.CTkFont(f"{font_entry_value}",25,'bold'))
        self.textbox.focus_force()
     

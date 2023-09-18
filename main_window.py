from CTkScrollableDropdown import *
import customtkinter as ctk
import json

ctk.set_appearance_mode("dark")
VALUES = list()
with open("fonts_families.json", "r") as fp:
    VALUES = json.load(fp=fp)

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
    def __init__(self, root, textbox:TextBoxLabel, font_entry:FontEntry):
        super().__init__(root,text="Change", font=ctk.CTkFont("Mooli", 10, "bold"))
        self.configure(command=self.change_font)
        self.grid(column=1, row=2,)
    def change_font(self,):
        font_entry_value = font_entry.get()
        font_entry.delete(0,  ctk.END)
        textbox.configure(font=ctk.CTkFont(f"{font_entry_value}",25,'bold'))
        textbox.focus_force()

                




    
root = Root()
# option_menu = OptionMenu(root)
# option_menu.configure(values=VALUES)
font_entry = FontEntry(root)
CTkScrollableDropdown(font_entry, values=VALUES,autocomplete=True, command=lambda e: font_entry.insert(0,e))
textbox_label = TextBoxLabel(root)
change_font_button = ChangeFontButton(root,textbox_label, font_entry)
textbox = TextBox(root)

root.mainloop()      

""" 
Here is the building or blueprint file where we make design and setting all the
attributes, methodes, and behavior or all widgets in app
"""
from CTkScrollableDropdown import CTkScrollableDropdown
import customtkinter as ctk
import json
from PIL import Image
from pathlib import Path
fil = Path(r"assets\\icons\\text.ico")

class Root(ctk.CTk):
    def __init__(self,**kwargs):
        super().__init__()
        self.title("Font-Viewer")
        self.geometry("700x400")
        self.resizable(0,0)
        self.iconbitmap(bitmap=fil)
        
        # set grid layout of root window app
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
      
class OptionMenu(ctk.CTkOptionMenu):
    def __init__(self, root):
        super().__init__(root,
                         variable=ctk.StringVar(value="Monotype Hadassah"),dropdown_font=ctk.CTkFont("Monotype Hadassah", 12, "bold"),width=100,)
        self.grid(column=1, row=1, )


class TextBoxLabel(ctk.CTkLabel):
    def __init__(self,root,textbox:ctk.CTkTextbox,**kwargs):
        super().__init__(root, text="Look at Your Font Effect Below", font=ctk.CTkFont("Mooli", 20, "bold"),corner_radius=0 )
        self.grid(column=0, row=0, pady=3, sticky="w")

class TextBox(ctk.CTkTextbox):
    def __init__(self,root:ctk.CTk,**kwargs):
        super().__init__(root,corner_radius=12, fg_color="white", text_color="#171717",font=ctk.CTkFont("Mooli", 20, "bold") )
        self.grid(column=0, row=2, rowspan=3, padx=6, sticky="ew")
        self.bind("<Motion>",lambda e:self.border_blue(e))
        self.bind("<Leave>", lambda e:self.reset_default_border_color_and_width(e))
        
    def border_blue(self,event):
        self.configure(border_color="blue") 
        self.configure(border_width=3) 
        print("Im in textbox")
        self.update()
        
    def reset_default_border_color_and_width(self,event):
        self.configure(border_color=["#979DA2", "#565B5E"]) 
        self.configure(border_width=0) 
        print("Im out of textbox")
        self.update()
        
class CurrentFontLabel(ctk.CTkLabel):
    def __init__(self,root:ctk.CTk,
                 current_font:TextBox,
                 **kwargs):
        
        super().__init__(root,
                         text=f"\nCurrent Font is set to: {current_font._font._family }\nCurrent size is set to: {current_font._font._size}\nCurrent weight is set to:{super(ctk.CTkFont,current_font._font).cget('weight')}", font=ctk.CTkFont("Mooli", 15, "bold"),
                         corner_radius=0, )
        self.grid(column=0, row=1 , sticky="w")
        self.current_font = current_font
        
class FontEntry(ctk.CTkEntry):
    def __init__(self,root:ctk.CTk):
        super().__init__(root, text_color="white",font=ctk.CTkFont("Mooli", 10, "bold"),placeholder_text="Choose your font here" )
        self.grid(column=1, row=1,)
        self.bind("<Motion>", lambda e:self.border_blue(e))
        self.bind("<Leave>", lambda e:self.reset_default_border_color(e))
    def border_blue(self,event):
        print("hey im in borderblue")
        self.configure(border_color="blue")
         
    def reset_default_border_color(self, event):
        print("hey im in reset_----")
        self.configure(border_color="gray65") 
     

class ChangeFontButton(ctk.CTkButton):
    def __init__(self, root, textbox:TextBoxLabel, font_entry:FontEntry,current_font:CurrentFontLabel,**kwargs):
        super().__init__(root,text="Change", font=ctk.CTkFont("Mooli", 10, "bold"),**kwargs)
        self.configure(command=self.change_font)
        self.grid(column=1, row=2,)
        self.font_entry = font_entry
        self.textbox = textbox
        self.current_font= current_font
        self.default_font = ctk.CTkFont("Mooli", 20, "bold")
    
    def prevent_null_string(self,font_entry_value):
        if font_entry_value == "":
            return "Mooli"
        else:
            return font_entry_value
 
    def change_font(self,):
        font_entry_value = self.prevent_null_string(self.font_entry.get())
        self.font_entry.delete(0,  ctk.END)
        self.textbox.configure(font=ctk.CTkFont(f"{font_entry_value}",25,'bold'))
        
        self.current_font.current_font._font.configure(family=self.textbox._font._family,size=self.textbox._font._size,weight=super(ctk.CTkFont, self.textbox._font).cget("weight"))
        self.current_font.current_font.update()
        self.current_font.configure(
            text=f"\nCurrent Font is set to:{self.current_font.current_font._font._family  }\nCurrent size is set to: {self.current_font.current_font._font._size}\nCurrent weight is set to:{super(ctk.CTkFont,self.current_font.current_font._font).cget('weight')}")
        self.textbox.focus_force()
        
     

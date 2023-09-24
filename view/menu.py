import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from view import img as imgService
from src import config as cfg
def setBG(self,root):
        self.root.title("Window with Background Image")
        self.root.geometry("800x800+2000+-100")

        self.img = Image.open(cfg.GAME_BOARD)
        self.bg_image = None

        self.background_label = tk.Label(root)
        self.background_label.pack(fill=tk.BOTH, expand=True)

def on_select_change(event,self):
    selected_index = self.select_box.get()
    check_and_set_elements(self,selected_index)
    imgService.setImages(self,imgService.trySetPathToimg("Places", selected_index,cfg.EMPTY_PLACES),self.imgPlaceWidth,self.imgPlaceHeight,self.placeImg)
    setTextintextPlacesElemen(self,selected_index)

def on_select_momnster_change(event,self):
    selected_index = self.selectboxmonster.get()
    setTextintextMonsterElemen(self, selected_index)
    imgService.setImages(self,imgService.trySetPathToimg("Beast", selected_index, cfg.EMPTY_BEAST),self.imgMonsterWidth,self.imgMonsterHeight,self.monsterImg)

def check_and_set_elements(self, value_to_find):
    if "places" in self.beastAndPlaces:
        places = self.beastAndPlaces["places"]
        if value_to_find in places:
            self.selectboxmonster['values'] = places[value_to_find]    
            self.selectboxmonster.current(0)
            self.selectboxmonster.bind("<<ComboboxSelected>>", lambda event, : on_select_momnster_change(event, self))
            
def setSelectBoxPlaces(self, root):
        self.select_box = ttk.Combobox(root,values=[place["name"] for place in self.places['places']])
        self.select_box.current(0)
        self.select_box.bind("<<ComboboxSelected>>", lambda event, : on_select_change(event, self))
        return self.select_box

def setSelectBoxMonster(self, root):
        self.select_box = ttk.Combobox(root)
        return self.select_box

def find_value_in_list_of_dicts(name_to_find, list_of_dicts):
    for item in list_of_dicts:
        if item.get("name") == name_to_find:
            return item
    return None  

def setTextintextMonsterElemen(self, key):
    try:
        dict_=find_value_in_list_of_dicts(key, self.beast['beast'])
        text=f"""Name: {dict_['name']}
Level: {dict_['level']}
Description: {dict_['description']}
Element: {', '.join(dict_['element'])}
Species: {', '.join(dict_['species'])}
Color: {', '.join(dict_['color'])}
"""
    except:
        text=""
    self.textPlacesElement["state"]="normal"
    self.textPlacesElement.delete(1.0, tk.END) 
    self.textPlacesElement.insert(tk.END, text)
    self.textPlacesElement["state"]="disabled"

def setTextintextPlacesElemen(self, key):
    dict_=find_value_in_list_of_dicts(key, self.places['places'])
    text=f"""Name: {dict_['name']}
Level: {dict_['level']}
Description: {dict_['description']}
Element: {', '.join(dict_['element'])}
"""
    self.textPlacesElement["state"]="normal"
    self.textPlacesElement.delete(1.0, tk.END) 
    self.textPlacesElement.insert(tk.END, text)
    self.textPlacesElement["state"]="disabled"

def settextPlacesElement(self, root):
    # Create a label
    self.textPlacesElement = tk.Text(root,state="disabled")
    
    return self.textPlacesElement
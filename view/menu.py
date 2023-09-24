import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from view import img as imgService
from src import config as cfg
from src import prompts as prompts
from tkinter import messagebox
import json
from src import midjourneyService

def exit_fullscreen(self, event):
    self.root.attributes("-fullscreen", False)  # Exit full-screen mode
    self.root.unbind("<Escape>")  # Remove the action bound to the Escape key

def load_places(self):
    with open(cfg.PROMPT_PLACES, "r") as json_file:
        self.places=json.load(json_file)

    with open(cfg.BEAST_AND_MONSTER, "r") as json_file:
        self.beastAndPlaces =json.load(json_file)
        
    with open(cfg.PROMPT_BEAST, "r") as json_file:
        self.beast =json.load(json_file)


def setBG(self,root):
        self.root.title("AI-Powered RPG World and Element Generator")
        self.root.attributes("-fullscreen", True)  # Set to full-screen mode
        self.root.bind("<Escape>", lambda event: exit_fullscreen(self,event))  # Allows exiting full-screen mode by pressing the Escape key


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

def createBtn(self, text):
    button = tk.Button(self.root, text=text)
    button.pack()
    return button

def bindGenerationBtn(self, btn):
    btn.bind("<Button-1>",lambda event: callAIgenrationAndShowResult(self) )

def setPlaceSelecBoxValues(self):
    load_places(self)
    self.selectboxplaces.values=[place["name"] for place in self.places['places']]

def callAIgenrationAndShowResult(self):
    # todo wrzucic do watku
    result=prompts.places_(1)
    messagebox.showinfo("Result",f"{result}")
    setPlaceSelecBoxValues(self)
    
def bindTest(self,btn):
    btn.bind("<Button-1>",lambda event: setPlaceSelecBoxValues(self))
    
def generateBeastImg(self):
    result=find_value_in_list_of_dicts(self.selectboxmonster.get(), self.beast['beast'])
    if result!=None:
        prompt=midjourneyService.generateBeastPrompt(result)
        midjourneyService.startGenrateImg(prompt,"Beast",result["name"].replace(' ', '_'))
        imgService.setImages(self,imgService.trySetPathToimg("Beast", self.selectboxmonster.get(), cfg.EMPTY_BEAST),self.imgMonsterWidth,self.imgMonsterHeight,self.monsterImg)
        
def bindBeastIMGGenBtn(self,btn):
    btn.bind("<Button-1>",lambda event: generateBeastImg(self))
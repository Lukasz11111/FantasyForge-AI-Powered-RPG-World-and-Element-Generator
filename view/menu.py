import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

def setBG(self,root):
        self.root.title("Window with Background Image")
        self.root.geometry("800x800")

        self.img = Image.open("./resources/img/game_board.png")
        self.bg_image = None

        self.background_label = tk.Label(root)
        self.background_label.pack(fill=tk.BOTH, expand=True)

def on_select_change(self, event):
    selected_index = self.get_selected_index()
    if selected_index >= 0:
        selected_place = self.places["places"][selected_index]["name"]
        print("Selected Place:", selected_place)
        # Update options for the second ComboBox based on the selected place
        self.secondSelect.set_values(
            self.beast_and_places["places"].get(selected_place, [])
        )
       
def setSelectBox(self, root):
        self.select_box = ttk.Combobox(root)
        self.select_box.place(relx=0.3, rely=0.1, anchor=tk.CENTER)
        self.select_box.bind("<<ComboboxSelected>>", on_select_change)
        self.select_box.set_values(
            [place["name"] for place in self.places['places']]
        )

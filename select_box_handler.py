import tkinter as tk
from tkinter import ttk

class SelectBoxHandler:
    def __init__(self, root, parent, beast_and_places,places,secondSelect=None):
        self.root = root
        self.parent = parent
        self.beast_and_places = beast_and_places
        self.places = places
        self.secondSelect=secondSelect
        self.select_var = tk.IntVar()
        self.select_box = ttk.Combobox(parent)
        self.select_box.bind("<<ComboboxSelected>>", self.on_select_change)

    def place(self, **kwargs):
        self.select_box.place(**kwargs)

    def set_values(self, values):
        self.select_box["values"] = values

    def get_selected_index(self):
        return self.select_box.current()

    def on_select_change(self, event):
        
        selected_index = self.get_selected_index()
        if selected_index >= 0:
            selected_place = self.places["places"][selected_index]["name"]
            print("Selected Place:", selected_place)
            # Update options for the second ComboBox based on the selected place
            print(dir(self.secondSelect))
            self.secondSelect.set_values(
                self.beast_and_places["places"].get(selected_place, [])
            )

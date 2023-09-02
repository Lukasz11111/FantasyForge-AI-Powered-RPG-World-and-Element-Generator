import tkinter as tk
from PIL import Image, ImageTk
import json
from select_box_handler import SelectBoxHandler
from view import menu as menu

class App:
    def __init__(self, root):
        self.root = root
        menu.setBG(self, root)
        self.load_places()
        menu.setSelectBox(self, root)
        # self.second_select_box_handler = SelectBoxHandler(self.root, root, {},self.places)
        # self.second_select_box_handler.place(relx=0.7, rely=0.1, anchor=tk.CENTER)

        # self.select_box_handler.place(relx=0.3, rely=0.1, anchor=tk.CENTER)

        self.root.bind("<Configure>", self.update_background)

    def load_places(self):
        with open("./prompt/places.json", "r") as json_file:
            self.places=json.load(json_file)

        with open("./prompt/beastAndPlaces.json", "r") as json_file:
            self.beastAndPlaces =json.load(json_file)

    def update_background(self, event):
        width, height = self.root.winfo_width(), self.root.winfo_height()
        resized_img = self.img.resize((width, height), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(resized_img)
        self.background_label.configure(image=self.bg_image)
        self.background_label.image = self.bg_image

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.run()

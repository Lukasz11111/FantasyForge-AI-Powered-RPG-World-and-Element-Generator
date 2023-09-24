import tkinter as tk
from PIL import Image, ImageTk
import json
from select_box_handler import SelectBoxHandler
from view import menu as menu
from view import img as imgService
from src import config as cfg

class App:
    
    def grid(self):
        self.selectboxplaces.place(relx=0.15, rely=0.1, anchor=tk.CENTER)
        self.selectboxmonster.place(relx=0.35, rely=0.1, anchor=tk.CENTER)
        self.textPlacesElement.place(relx=0.7, rely=0.2, anchor=tk.CENTER,width=400,height=200)
        self.imgPlaceWidth=350
        self.imgPlaceHeight=350
        self.placeImg.place(relx=0.28,  rely=0.65, anchor=tk.CENTER,width=self.imgPlaceWidth,height=self.imgPlaceHeight)
        self.imgMonsterWidth=350
        self.imgMonsterHeight=350
        self.monsterImg.place(relx=0.72, rely=0.65, anchor=tk.CENTER,width=self.imgMonsterWidth,height=self.imgMonsterHeight)
        self.btnGenerate.place(relx=0.15, rely=0.13, anchor=tk.CENTER)
        self.btnDelete.place(relx=0.15, rely=0.16, anchor=tk.CENTER)
        self.btnTest.place(relx=0.15, rely=0.19, anchor=tk.CENTER)
        self.btnBeastImage.place(relx=0.72, rely=0.83, anchor=tk.CENTER)
        
    def __init__(self, root):
        self.root = root
        menu.setBG(self, root)
        menu.load_places(self)
        # Create all componets
        self.selectboxmonster=menu.setSelectBoxMonster(self, root)
        self.selectboxplaces=menu.setSelectBoxPlaces(self, root)
        self.textPlacesElement=menu.settextPlacesElement(self, root)
        self.placeImg=imgService.setImgFrame(root)
        self.monsterImg=imgService.setImgFrame(root)
        self.btnGenerate=menu.createBtn(self, "Generate Place And Beast (only prompt)")
        self.btnDelete=menu.createBtn(self, "Delete select Place And all beast from this place")
        self.btnBeastImage=menu.createBtn(self, "Crate beast image")
        self.btnTest=menu.createBtn(self, "test")
        
    
        #todo
        # btn usuwania miejsca besti i obu
        # btn genrowania  miejsca i besti
        # btn genrowania obrazow
        
        # Set place to all componets
        self.grid()
        # Set images (must be after grid() because images will be resized)
        imgService.setImages(self,cfg.EMPTY_PLACES,self.imgPlaceWidth,self.imgPlaceHeight,self.placeImg)
        imgService.setImages(self,cfg.EMPTY_BEAST,self.imgMonsterWidth,self.imgMonsterHeight,self.monsterImg)
        menu.bindGenerationBtn(self,self.btnGenerate)
        menu.bindTest(self,self.btnTest)
        menu.bindBeastIMGGenBtn(self,self.btnBeastImage)
        self.root.bind("<Configure>", self.update_background)


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

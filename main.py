import tkinter as tk
from PIL import Image, ImageTk

def set_background_image(image_path):
    global background_label, bg_image, img
    img = Image.open(image_path)
    update_background()

def update_background():
    width, height = app.winfo_width(), app.winfo_height()
    resized_img = img.resize((width, height), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(resized_img)
    background_label.configure(image=bg_image)
    # Keep a reference to the image to prevent it from being garbage collected
    background_label.image = bg_image

app = tk.Tk()
app.title("Window with a Background Image")

############# Set the base window size to 500x500 #############
app.geometry("800x800")

default_image_path = "./resources/img/game_board.png"
img = Image.open(default_image_path)

background_label = tk.Label(app)
background_label.pack(fill=tk.BOTH, expand=True)

update_background()

app.bind("<Configure>", lambda event: update_background())

app.mainloop()
